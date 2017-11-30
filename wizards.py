from __future__ import print_function
import math
import random
from simanneal import Annealer
from random import shuffle

class NonBetweenness(Annealer):
    def __init__(self, num_wizards, num_constraints, wizards, constraints):
        shuffle(wizards)
        super(NonBetweenness, self).__init__(wizards) #initializes state of super class
        # mapping for efficient position lookup by wizard name
        self.wiz_to_pos = {wizards[i] : i for i in range(len(wizards))}
        self.num_wizards = num_wizards
        self.num_constraints = num_constraints
        self.constraints = constraints
        # NOTE: state == wizards

    def move(self):
        """Swaps two wizard assignments."""
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.wiz_to_pos[self.state[a]], self.wiz_to_pos[self.state[b]] = self.wiz_to_pos[self.state[b]], self.wiz_to_pos[self.state[a]]
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def energy(self):
        """Calculates the number of constraints unsatisfied."""
        e = 0
        for wizard in self.state:
            for c in self.constraints:
                x, y, z = self.wiz_to_pos[c[0]], self.wiz_to_pos[c[1]], self.wiz_to_pos[c[2]]
                if wizard == c[2] and (x < z < y or y < z < x):
                    e += 1
        return e


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
