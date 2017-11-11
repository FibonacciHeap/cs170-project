from input_generator import DifficultInputGenerator
from constraint_generator import ConstraintGenerator
from solver import MagicianAgeOrderingSolver

N = 4
constraint_constructor = ConstraintGenerator(N, ConstraintGenerator.RANDOM)
problem_solver = MagicianAgeOrderingSolver(N, MagicianAgeOrderingSolver.RANDOM)
input_generator = DifficultInputGenerator(constraint_constructor.generate, \
                                          problem_solver.solve)

ratio = input_generator.find_best_constraint_to_magicians_ratio(N)
print("The best k to n ratio is: {0}".format(ratio))
