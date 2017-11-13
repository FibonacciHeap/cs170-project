from input_generator import DifficultInputGenerator
from constraint_generator import ConstraintGenerator
from solver import MagicianAgeOrderingSolver

RATIO = 2.4

def generate_constraint(constraint_constructor):
    valid = True
    while True:
        constraints = constraint_constructor.generate(int(RATIO * n + 1))
        for constraint in constraints:
            _constraint = [int(i) for i in constraint]
            if (_constraint[0] < _constraint[2] < _constraint[1]) or (_constraint[1] < _constraint[2] < _constraint[0]):
                valid = False
            elif _constraint[0] == _constraint[2] or _constraint[0] == _constraint[1] or _constraint[1] == _constraint[2]:
                valid = False
        if valid:
            break
    return constraints

def generate_input():
    n_list = [20, 35, 50]
    for n in n_list:
        constraint_constructor = ConstraintGenerator(n,\
            ConstraintGenerator.RANDOM)
        constraints = generate_constraint(constraint_constructor)
        with open("input" + str(n) + ".in", "a") as f:
            ans = [" ".join(c) for c in constraints]
            print(ans)
            for a in ans:
                f.write(a)
                f.write('\n')

generate_input()
