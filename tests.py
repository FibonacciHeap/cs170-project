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
            self.num_wizards,
            ConstraintGenerator.SINGLE_SIDE_NEIGHBOR,
        )
        self.balanced_cg = ConstraintGenerator(
            self.num_wizards,
            ConstraintGenerator.BALANCED,
        )
        self.inward_merge_cg = ConstraintGenerator(
            self.num_wizards,
            ConstraintGenerator.INWARD_MERGE,
        )

    def test_random_cg(self):
        constraints = self.random_cg.generate(self.num_constraints)
        # test generated constraints are valid
        for constraint in constraints:
            _constraint = [int(i) for i in constraint]
            self.assertFalse(_constraint[0] < _constraint[2] < _constraint[1])
            self.assertFalse(_constraint[1] < _constraint[2] < _constraint[0])

        # test each group of NUM_WIZARDS constraints have unique target wizards
        wizards_picked = set()
        for i, constraint in enumerate(constraints):
            if i % self.num_wizards == 0:
                wizards_picked = set()
            self.assertNotIn(constraint[2], wizards_picked)
            wizards_picked.add(constraint[2])

        # test that known solution satisfies all constraints
        for i in range(self.num_wizards):
            wizard = str(i)
            for constraint in constraints:
                if constraints[2] == wizard:
                    self.assertFalse(constraint[0] < wizard < constraint[1])
                    self.assertFalse(constraint[1] < wizard < constraint[0])

    def test_ssn_cg(self):
        constraints = self.ssn_cg.generate(self.num_constraints)

        for constraint in constraints:
            _constraint = [int(i) for i in constraint]
            # test generated constraints are valid
            self.assertFalse(_constraint[0] < _constraint[2] < _constraint[1])
            self.assertFalse(_constraint[1] < _constraint[2] < _constraint[0])
            # test each constraint is from a group of 3 adjacent wizards
            self.assertTrue(abs(_constraint[2] - _constraint[0]) <= 2)
            self.assertTrue(abs(_constraint[1] - _constraint[0]) <= 2)

        # test that known solution satisfies all constraints
        for i in range(self.num_wizards):
            wizard = str(i)
            for constraint in constraints:
                if constraints[2] == wizard:
                    self.assertFalse(constraint[0] < wizard < constraint[1])
                    self.assertFalse(constraint[1] < wizard < constraint[0])

    def test_balanced_cg(self):
        pass

    def test_inward_merge_cg(self):
        constraints = self.inward_merge_cg.generate(self.num_constraints)

        for constraint in constraints:
            _constraint = [int(i) for i in constraint]
            # test generated constraints are valid
            self.assertFalse(_constraint[0] < _constraint[2] < _constraint[1])
            self.assertFalse(_constraint[1] < _constraint[2] < _constraint[0])

        # test that known solution satisfies all constraints
        for i in range(self.num_wizards):
            wizard = str(i)
            for constraint in constraints:
                if constraints[2] == wizard:
                    self.assertFalse(constraint[0] < wizard < constraint[1])
                    self.assertFalse(constraint[1] < wizard < constraint[0])


if __name__ == '__main__':
    unittest.main()
