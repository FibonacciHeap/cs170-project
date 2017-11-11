from input_generator import DifficultInputGenerator
from constraint_generator import ConstraintGenerator
from solver import MagicianAgeOrderingSolver

N = 5
K = 100

print("Running experiment for RANDOM Constraint Strategy.")
constraint_constructor = ConstraintGenerator(N, ConstraintGenerator.RANDOM)
problem_solver = MagicianAgeOrderingSolver(N, MagicianAgeOrderingSolver.RANDOM)
input_generator = DifficultInputGenerator(constraint_constructor.generate, \
                                          problem_solver.solve, K)

ratio = input_generator.find_best_constraint_to_magicians_ratio(N)
print("The best k to n ratio is: {0}\n\n".format(ratio))


print("Running experiment for SINGLE_SIDE_NEIGHBOR Constraint Strategy.")
constraint_constructor = ConstraintGenerator(N, ConstraintGenerator.SINGLE_SIDE_NEIGHBOR)
problem_solver = MagicianAgeOrderingSolver(N, MagicianAgeOrderingSolver.RANDOM)
input_generator = DifficultInputGenerator(constraint_constructor.generate, \
                                          problem_solver.solve, K)

ratio = input_generator.find_best_constraint_to_magicians_ratio(N)
print("The best k to n ratio is: {0}\n\n".format(ratio))


print("Running experiment for INWARD_MERGE Constraint Strategy.")
constraint_constructor = ConstraintGenerator(N, ConstraintGenerator.INWARD_MERGE)
problem_solver = MagicianAgeOrderingSolver(N, MagicianAgeOrderingSolver.RANDOM)
input_generator = DifficultInputGenerator(constraint_constructor.generate, \
                                          problem_solver.solve, K)

ratio = input_generator.find_best_constraint_to_magicians_ratio(N)
print("The best k to n ratio is: {0}\n\n".format(ratio))
