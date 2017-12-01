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
        self.Tmax = 600000.0
        self.Tmin = 2.5
        self.steps = 1000000
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

    def _move_adjacently(self):
        a = randint(0, len(self.state) - 1)
        if a == 0:
            b = a + 1
        elif a == len(self.state) - 1:
            b = a - 1
        else:
            offset = choice[1, -1]
            b = a + offset
        _swap_wizards(self.state[a], self.state[b])

    def _move_satisfy_random_constraint(self):
        """Satisfies a random unsatisfied constraint."""
        secure_random = random.SystemRandom()
        done = False
        while not done:
            c = secure_random.choice(self.constraints)
            if self._is_constraint_violated(c):
                done = True
                # swap 2 wizards to move closer
                self.state[c[1]], self.state[c[2]] = self.state[c[2]], self.state[c[1]]
                self.wiz_to_pos[c[1]], self.wiz_to_pos[c[2]] = self.wiz_to_pos[c[2]], self.wiz_to_pos[c[1]]
                # with probability 0.5, swap the two border wizards
                if random.randint(0, 1) == 1:
                    """incomplete"""

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

# if __name__ == '__main__':
#
#     # latitude and longitude for the twenty largest U.S. cities
#     cities = {
#         'New York City': (40.72, 74.00),
#         'Los Angeles': (34.05, 118.25),
#         'Chicago': (41.88, 87.63),
#         'Houston': (29.77, 95.38),
#         'Phoenix': (33.45, 112.07),
#         'Philadelphia': (39.95, 75.17),
#         'San Antonio': (29.53, 98.47),
#         'Dallas': (32.78, 96.80),
#         'San Diego': (32.78, 117.15),
#         'San Jose': (37.30, 121.87),
#         'Detroit': (42.33, 83.05),
#         'San Francisco': (37.78, 122.42),
#         'Jacksonville': (30.32, 81.70),
#         'Indianapolis': (39.78, 86.15),
#         'Austin': (30.27, 97.77),
#         'Columbus': (39.98, 82.98),
#         'Fort Worth': (32.75, 97.33),
#         'Charlotte': (35.23, 80.85),
#         'Memphis': (35.12, 89.97),
#         'Baltimore': (39.28, 76.62)
#     }
#
#     # initial state, a randomly-ordered itinerary
#     init_state = list(cities.keys())
#     random.shuffle(init_state)
#
#     # create a distance matrix
#     distance_matrix = {}
#     for ka, va in cities.items():
#         distance_matrix[ka] = {}
#         for kb, vb in cities.items():
#             if kb == ka:
#                 distance_matrix[ka][kb] = 0.0
#             else:
#                 distance_matrix[ka][kb] = distance(va, vb)
#
#     tsp = TravellingSalesmanProblem(init_state, distance_matrix)
#     tsp.steps = 100000
#     # since our state is just a list, slice is the fastest way to copy
#     tsp.copy_strategy = "slice"
#     state, e = tsp.anneal()
#
#     while state[0] != 'New York City':
#         state = state[1:] + state[:1]  # rotate NYC to start
#
#     print()
#     print("%i mile route:" % e)
#     for city in state:
#         print("\t", city)
