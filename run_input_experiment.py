from input_generator import DifficultInputGenerator
from constraint_generator import ConstraintGenerator
from solver import MagicianAgeOrderingSolver

N = 10
constraint_constructor = ConstraintGenerator(ConstraintGenerator.RANDOM)
problem_solver = MagicianAgeOrderingSolver(MagicianAgeOrderingSolver.RANDOM)
input_generator = DifficultInputGenerator(constraint_constructor.generate, \
                                          problem_solver.solve)
                                        
ratio = input_generator.find_best_constraint_to_magicians_ratio(N)
print("The best k to n ratio is: {0}".format(ratio))
