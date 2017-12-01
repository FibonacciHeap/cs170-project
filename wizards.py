from __future__ import print_function
import math
from random import (
    randint,
    shuffle,
    choice,
)

import random
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/simanneal-master/simanneal')
from anneal import Annealer

class NonBetweenness(Annealer):
    def __init__(self, num_wizards, num_constraints, wizards, constraints):
        # NOTE: state == wizards
        shuffle(wizards)
        super(NonBetweenness, self).__init__(wizards)
        # set hyperparameters
        self.Tmax = 1000000.0
        self.Tmin = 0.8
        self.steps = 50000
        self.updates = 1000
        # mapping for efficient position lookup by wizard name
        self.wiz_to_pos = {wizards[i] : i for i in range(len(wizards))}
        self.num_wizards = num_wizards
        self.num_constraints = num_constraints
        self.constraints = constraints

    def energy(self):
        """Calculates the number of constraints unsatisfied."""
        return sum([1 for c in self.constraints if self._is_constraint_violated(c)])

    def move(self):
        """Performs a move during the simmulated annealing algorithm."""
        self._move_satisfy_random_constraint()
        #self._move_randomly()
        #self._move_adjacently()

    def _move_adjacently(self):
        a = randint(0, len(self.state) - 1)
        if a == 0:
            b = a + 1
        elif a == len(self.state) - 1:
            b = a - 1
        else:
            offset = choice([1, -1])
            b = a + offset
        self._swap_wizards(self.state[a], self.state[b])


    def _move_range_shuffle(self, range_len):
        """Shuffles a random, continuous subset of the current state, provided the length of the range desired to be shuffled"""
        #start1 = randint(range_len, len(self.state) - range_len)
        start = randint(0, len(self.state) - range_len)
        #range_list = choice([[start1, start1 - range_len], [start2, start2 + range_len]])
        end = start + range_len

        copy_state = self.state[start:end]
        random.shuffle(copy_state)
        self.state[start:end] = copy_state

        for wizard in self.state[start:end]:
            self.wiz_to_pos[wizard] = self.state.index(wizard)


    def _move_satisfy_random_constraint(self):
        """Satisfies a random unsatisfied constraint."""
        secure_random = random.SystemRandom()
        done = False
        while not done:
            c = secure_random.choice(self.constraints)
            if self._is_constraint_violated(c):
                done = True
                # swap 2 wizards to move closer
                self._swap_wizards(c[random.randint(0, 1)], c[2])
                # with probability 0.5, swap the two border wizards
                # if random.randint(0, 1) == 1:
                #     self._swap_wizards(c[0], c[1])

    def _move_randomly(self):
        """Swaps two wizard assignments."""
        a, b = randint(0, len(self.state) - 1), randint(0, len(self.state) - 1)
        wiz1, wiz2 = self.state[a], self.state[b]
        self._swap_wizards(wiz1, wiz2)

    def _swap_wizards(self, wiz1, wiz2):
        pos1, pos2 = self.wiz_to_pos[wiz1], self.wiz_to_pos[wiz2]
        self.state[pos1], self.state[pos2] = self.state[pos2], self.state[pos1]
        self.wiz_to_pos[wiz1], self.wiz_to_pos[wiz2] = self.wiz_to_pos[wiz2], self.wiz_to_pos[wiz1]

    def _is_constraint_violated(self, c):
        return (
            (self.wiz_to_pos[c[0]] < self.wiz_to_pos[c[2]] < self.wiz_to_pos[c[1]]) or
            (self.wiz_to_pos[c[1]] < self.wiz_to_pos[c[2]] < self.wiz_to_pos[c[0]])
        )
