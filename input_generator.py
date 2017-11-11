import time
import logging
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

class DifficultInputGenerator:
    """
    Difficult Input Generator

    Collection of routines that *tries* to discover and construct inputs to the
    Magician Age Ordering problem with the *believed* characteristics of a
    computationally hard one.

    """

    MAX_NUM_CONSTRAINTS = 500

    def __init__(self, generate_constraint, solve_problem):
        """
        Constructs the Input Generator object given a constraint generation
        function (which returns a set of constraints given a number of magicians
        and a number of constraints) and a problem solver (which returns a valid
        ordering, time until first solution, and number of total solutions).
        """
        self.generate_constraint = generate_constraint
        self.solve_problem = solve_problem

    def find_best_constraint_to_magicians_ratio(self, n, start_k = 1, reps = 1000):
        """
        This routine will find the number of constraints k that makes a problem
        of size n take the most time while having the least number of possible
        solutions (which we are heuristically believing that will correlate most
        with a computationally hard input for the Magician Age Ordering problem).

        This function will try to generate reps number of valid constraints
        (following a heuristic defined during the object construction) for all
        possible number of constraint k from 1 to 500, solve the Magician Age
        Ordering (with some strategy defined on the object construction), and
        store the average *time to first solution* and *total solution count*
        for each k, and then decide based on these metrics what is the best
        value for k.

        Input:
            n: number of magicians in the input problem
            reps: number of experiments ran for each number of constraints k

        Output:
            ratio: the best number of constraint k divided by the number of
                   magicians n
        """
        # 1. Perform experiments
        logging.debug("Experiment: n = {0}, k = {1}".format(n, start_k))
        avg_first_tictoc_list, avg_solution_count_list = [], []
        k_list = list(range(start_k, self.MAX_NUM_CONSTRAINTS))
        for k in k_list:
            logging.debug("Trying k = {0}".format(k))
            avg_first_tictoc, avg_solution_count = 0, 0
            for _ in range(reps):
                print("Iteration {0}/{1}".format(_ + 1, reps), end='\r')
                constraints = self.generate_constraint(k)
                if constraints is None:
                    # We should only reach here if k is a number such that no
                    # valid input problem of size n and k constraints can be
                    # generated.
                    break
                first_tictoc, solution_count = self.solve_problem(constraints)
                avg_first_tictoc += first_tictoc
                avg_solution_count += solution_count
            avg_first_tictoc /= reps
            avg_solution_count /= reps
            avg_first_tictoc_list.append(avg_first_tictoc)
            avg_solution_count_list.append(avg_solution_count)

        # 2. Save experiments
        result_logs = {
            "MagicianNumber": n,
            "AverageFirstTictocList": avg_first_tictoc_list,
            "AverageSolutionCountList": avg_solution_count_list
        }
        self.save_results(result_logs)

        # 3. Plot results
        self.show_plot("k vs. Average Solution Count", k_list,
            avg_solution_count_list, "k", "Avg Solution Count")
        scaled_avg_first_tictoc_list = [i/j for i, j in \
            zip(avg_first_tictoc_list, k_list)]
        self.show_plot("k vs. Scaled Average Time to First Solution", k_list,
            scaled_avg_first_tictoc_list, "k", "Scaled Avg Time to 1st Solution")
        self.show_plot("k vs. Average Time to First Solution", k_list,
            avg_first_tictoc_list, "k", "Avg Time to 1st Solution", "r")

        # 4. Analyze and return final result
        best_k_1 = np.argmin(avg_solution_count_list) + 1
        print("Best k based on figure 1: {0}".format(best_k_1))
        best_k_2 = np.argmax(scaled_avg_first_tictoc_list) + 1
        print("Best k based on figure 2: {0}".format(best_k_2))

        avg_best_k = best_k_1 + best_k_2 // 2 # not necessarily true, but...
        final_ratio = avg_best_k / n
        return final_ratio

    def save_results(self, results, filename = 'saved_results.txt'):
        """
        Save results from an experiment in a file.
        """
        with open(filename, "a") as f:
            ts = time.time()
            timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            f.write("{0} --- {1}\n\n\n".format(timestamp, results))

    def show_plot(self, title, x, y, xlabel, ylabel, color='g'):
        """
        Plot x vs y.
        """
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def find_solution_number_variation_for_each_constraint_number(self):
        pass
