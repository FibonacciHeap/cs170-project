import time
from datetime import datetime
from random import shuffle
import itertools

class MagicianAgeOrderingSolver(object):

    """
    Magician Age Ordering Solver Class

    Methods to take the constraints generated from our
    constaints generator and checks all possible orderings
    of our n magicians against the generated constaints.

    The number of possible solutions (orderings) is returned
    in addition to the time taken to find the number of solutions.
    """

    """Enum constants for generator type"""
    RANDOM = 0
    SINGLE_SIDE_NEIGHBOR = 1
    BALANCED = 2
    INWARD_MERGE = 3


    def __init__(self, n, generator_type=0):
        self.num_wizards = n
        self.gen_type = generator_type
        self.wizard_list = [str(i) for i in range(self.num_wizards)]
        self.wizard_permutations = self.generate_permutations()
        shuffle(self.wizard_permutations)

    def solve(self, constraints):
        """
        This function will iterate through all possible ordering of our wizard list,
        and given the constraints that we have generated, will test the ordering for validity.
        """
        solution_count = 0
        solution_found = False

        #t2 is initially set to t1, if no asnwer is found, the time will be zero.
        t1 = time.time()
        t2 = t1

        for wizard_ordering in self.wizard_permutations:
            if self.check_constraints(wizard_ordering, constraints):
                solution_count +=1
                if (not solution_found):
                    solution_found = True
                    t2 = time.time()
        return t2 - t1, solution_count

    def generate_permutations(self):
        """
        Returning all possible permutations of the original list of wizards that we have.
        """
        return list(itertools.permutations(self.wizard_list))


    def check_constraints(self, wizard_ordering, constraints):
        """
        This function checks a given ordering against our generated constraints
        and that the wizards fall in locations valid for this. c is the constraint tuple.
        """

        d = {k: v for v, k in enumerate(wizard_ordering)}

        for c in constraints:
            if not ((d[c[2]] < d[c[1]]
                and  d[c[2]] < d[c[0]])
                or  (d[c[2]] > d[c[1]]
                and  d[c[2]] > d[c[0]])):
            	return False
        return True
