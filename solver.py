import argparse
from itertools import groupby

from wizards import NonBetweenness

"""
======================================================================
  Complete the following function.
======================================================================
"""

def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints,
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    print("Num constraints before removing duplicates: ", len(constraints))
    for constraint in constraints:
        # sort the first two elements in the list
        constraint[0], constraint[1] = min(constraint[0], constraint[1]), \
            max(constraint[0], constraint[1])
    # remove duplicates
    constraints = [k for k,v in groupby(sorted(constraints))]
    print("Num constraints before after duplicates: ", len(constraints))
    solver = NonBetweenness(num_wizards, num_constraints, wizards, constraints)
    wizard_assignment_array = solver.anneal()
    print("\nBest energy for this iteration is: " + str(solver.best_energy))
    return wizard_assignment_array

"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)

    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)
