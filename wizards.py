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
    def __init__(self, identifier, num_wizards, num_constraints, wizards, constraints, outfile):
        # NOTE: state == wizards
        # shuffle(wizards) # do not shuffle because we may start with an ordering
        super(NonBetweenness, self).__init__(wizards)
        # set hyperparameters
        self.Tmax = 2.0
        self.Tmin = 0.08
        self.steps = 100000
        self.updates = 1500
        # self.randomize_hyperparams() # use this for exploring

        # mapping for efficient position lookup by wizard name
        self.identifier = identifier
        self.wiz_to_pos = {wizards[i] : i for i in range(len(wizards))}
        self.num_wizards = num_wizards
        self.num_constraints = num_constraints
        self.constraints = constraints
        self.wizards = wizards
        self.outfile = outfile

    def randomize_hyperparams(self):
        self.Tmax = random.uniform(2.5, 5)
        self.Tmin = random.uniform(0.01, 1)
        self.steps = randint(20000, 200000)
        self.updates = 100

    def energy(self):
        """Calculates the number of constraints unsatisfied."""
        E = sum([1 for c in self.constraints if self._is_constraint_violated(c)])
        if E == 0:
            self._save_solution()
            print("exiting...")
            exit()
        return E

    def move(self):
        """Performs a move during the simmulated annealing algorithm."""
        self._move_range_shuffle(3)
        self._move_satisfy_random_constraint()
        # self._move_range_shuffle(3)
        #if (curr_energy > 50):
        #    self._move_satisfy_random_constraint()
        #else:
        #    self._move_range_shuffle(3)

    def print_violated_constraints(self):
        for c in self.constraints:
            if self._is_constraint_violated(c):
                print(c)

    def _save_solution(self):
        print("FOUND OPTIMAL:", self.state)
        print("saving to file...", self.outfile)
        with open(self.outfile, 'w') as file:
            for w in self.state:
                file.write("{0} ".format(w))

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

    def dict_check(self):
        enum_dict = {v:i for i, v in enumerate(self.state)}
        error = 0
        for wizard in self.state:
            if (enum_dict[wizard] != self.wiz_to_pos[wizard]):
                error+=1
                print(wizard)
        return error

    def _move_range_shuffle(self, range_len):
        """Shuffles a random, continuous subset of the current state, provided the length of the range desired to be shuffled"""
        start = randint(0, len(self.state) - range_len)
        end = start + range_len

        # print("start: " + str(start))
        # print("end: " + str(end))
        # print("range_len: " + str(range_len))
        # print("prior state: ", self.state)
        # print("prior dict: ", self.wiz_to_pos)

        copy_state = self.state[start:end]

        #for wizard in copy_state:
        #    print(wizard)

        random.shuffle(copy_state)

        for i, wizard in enumerate(copy_state):
            #print("wiz1_loop: " + wizard)
            self.state[start + i] = wizard
            self.wiz_to_pos[wizard] = start + i

        # print("post state: ", self.state)
        # print("post dict: ", self.wiz_to_pos)
        # print('\n Error:', self.dict_check())
        # print("end\n \n")



    def _move_range_mirror(self, range_len):
        """Shuffles a random, continuous subset of the current state, provided the length of the range desired to be shuffled"""
        #start1 = randint(range_len, len(self.state) - range_len)
        start = randint(0, len(self.state) - range_len)
        #range_list = choice([[start1, start1 - range_len], [start2, start2 + range_len]])
        end = start + range_len

        copy_state = self.state[start:end]
        copy_state.reverse()
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
                if random.randint(0, 1) == 1:
                    self._swap_wizards(c[0], c[1])
        if not done: print("Nothing to do...")

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
