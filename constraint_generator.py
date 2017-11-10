import random

class ConstraintGenerator:
    """Enum constants for generator type"""
    RANDOM = 0
    SINGLE_SIDE_NEIGHBOR = 1
    # Add more as necessary here

    def ___init__(self, n, generator_type=ConstraintGenerator.RANDOM):
        """
        Input:
            n: number of magicians in the input problem
        """
        self.num_wizards = n
        self.gen_type = gen_type
        # could change later to actual names if desired
        self.wizards = [str(i) for i in range(num_wizards)]

    def generate(self, k):
        """
        Dispatch routine to call the appropriate Constraint Generator function
        """
        if self.gen_type = ConstraintGenerator.RANDOM:
            return self._generate_random(k)
        elif self.gen_type = ConstraintGenerator.SINGLE_SIDE_NEIGHBOR:
            return self._generate_single_side_neighbor(k)
        # Add more as necessary here

    def _generate_random(self, k):
        """
        Input:
            k: number of constraints to generate

        Output:
            constraints: a list of 3-tuples of type string, where each
            3-tuple is of the form (wizard_1, wizard_2, wizard_3),
            corresponding to the constraint:
            !(wizard_1 < wizard_3 < wizard_2 or wizard_2 < wizard_3 < wizard_1)
        """
        # Tracks how many times each wizard has been used as a
        # right-hand variable in a constraint, in order to enforce
        # the heuristic that repeated use makes the problem easier.
        selected_count_to_wizard_list = {
            i: list() for i in range(1, k // self.num_wizards + 1)
        }
        selected_count_to_wizard_list[0] = [
            self.wizards[i] for i in range(self.num_wizards)
        ]
        current_level = 0
        constraints = []
        for i in range(k):
            # Pick a target wizard for our constraint. Selection should be
            # uniformly random from the lowest possible selection level.
            target = random.choice(
                selected_count_to_wizard_list[current_level]
            )
            target_index = self.wizards.index(target)
            selected_count_to_wizard_list[current_level + 1].append(
                selected_count_to_wizard_list[current_level].pop(target)
            )
            if not selected_count_to_wizard_list[current_level]:
                current_level += 1

            # Pick two other wizards for the constraint. Can be a random
            # selection of any two that satisfy the following criteria:
            # 1: The two wizards are not the same and are not TARGET
            # 2: The two wizards are both from the SAME side of TARGET
            # 3: The two wizards are chosen from the larger free side of TARGET
            selection_range = (0, self.num_wizards - 1)
            if target_index < self.num_wizards / 2:
                selection_range[0] = target_index + 1
            else:
                selection_range[1] = target_index - 1
            first, second = None, None
            while first != second:
                first, second = randint(*selection_range), randint(*selection_range)
            first, second = self.wizards[first], self.wizards[second]

            constraints.append([first, second, target])

        return constraints

    def _generate_single_side_neighbor(self, k):
        if self.num_wizards < 4:
            raise ValueError("This generator requires a value of N >= 4")
        constraints = []
        for i in range(self.num_wizards - 2):
            constraints.append([
                self.wizards[i + 1],
                self.wizards[i + 2],
                self.wizards[i],
            ])
        constraints.append([
            self.wizards[self.num_wizards - 4],
            self.wizards[self.num_wizards - 3],
            self.wizards[self.num_wizards - 2],
        ])
        constraints.append([
            self.wizards[self.num_wizards - 3],
            self.wizards[self.num_wizards - 2],
            self.wizards[self.num_wizards - 1],
        ])
        return constraints
