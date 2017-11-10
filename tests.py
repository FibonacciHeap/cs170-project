import unittest

from constraint_generator import ConstraintGenerator

class TestConstraintGenerator(unittest.TestCase):
    def setUp(self):
        self.num_wizards = 10
        self.num_constraints = 30
        self.random_cg = ConstraintGenerator(
            self.num_wizards, ConstraintGenerator.RANDOM
        )
        self.ssn_cg = ConstraintGenerator(
            self.num_wizards, ConstraintGenerator.SINGLE_SIDE_NEIGHBOR
        )

    def test_random_cg(self):
        constraints = self.random_cg.generate(self.num_constraints)
        # test generated constraints are valid
        for constraint in constraints:
            self.assertFalse(constraint[0] < constraint[2] < constraint[1])
            self.assertFalse(constraint[1] < constraint[2] < constraint[0])

        # test each group of NUM_WIZARDS constraints have unique target wizards
        wizards_picked = set()
        for i, constraint in enumerate(constraints):
            if i % self.num_wizards == 0:
                wizards_picked = set()
            self.assertNotIn(constraint[2], wizards_picked)
            wizards_picked.add(constraint[2])

    def test_ssn_cg(self):
        pass


if __name__ == '__main__':
    unittest.main()
