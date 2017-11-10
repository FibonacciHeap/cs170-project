import time
from datetime import datetime
import itertools

class MagicianAgeOrderingSolver(object):

	"""
	Magician Age Ordering Solver Class
	
	Methods to take the constraints generated from our
	constaints generator and checks all possible orderings
	of our n magicians against the generated constaints.

	The number of possible solutions (orderings) is returned
	in addition to the time taken to find the number of solutions.
	"""

	"""Enum constants for generator type"""
	RANDOM = 0
	SINGLE_SIDE_NEIGHBOR = 1
	BALANCED = 2
	INWARD_MERGE = 3


	def __init__(self, n, generator_type=0):
		self.num_wizards = n
		self.gen_type = generator_type
		self.wizard_list = [str(i) for i in range(self.num_wizards)]
		self.wizard_permutations = self.generate_permutations()

	def solve(self, constraints):
		"""
		This function will iterate through all possible ordering of our wizard list,
		and given the constraints that we have generated, will test the ordering for validity.  
		"""
		solution_count = 0
		t1 = time.time()
		for wizard_ordering in self.wizards_permutations:
			if check_constraints(wizard_ordering, constraints):
				solution_count +=1

		t2 = time.time()
		return t2 - t1, solution_count
							
	def generate_permutations(self):
		"""
		Returning all possible permutations of the original list of wizards that we have.
		"""
		return list(itertools.permutations(self.wizard_list))
		
	def check_constraints(self, wizard_ordering, c):
		"""
		This function checks a given ordering against our generated constraints 
		and that the wizards fall in locations valid for this. c is the constraint tuple.
		"""
		for c in contraints:
			if ((wizard_ordering.index(c[1]) < wizard_ordering.index(c[0]) 
				and  wizard_ordering.index(c[1]) < wizard_ordering.index(c[2])) 
				or  (wizard_ordering.index(c[1]) > wizard_ordering.index(c[0]) 
				and  wizard_ordering.index(c[1]) > wizard_ordering.index(c[2]))):
				return false
		return true

