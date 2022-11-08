import sys
import timeit
import math
from solution import *

class StaircaseSolver:
    """
    A class for helping facilitate testing. Takes a list of tuples and a method.
    Tests that the use cases evaluate properly on the provided method

    Args
    method - the method from solution.py that is being tested against the use cases
    use_cases - a list of tuples where tuple[1] is the expected result of method(tuple[0])
    (ie, tuple = (method_input, output))

    Returns
    Nothing. If there is an assertion error, print the input, expected result, and actual result.
    If there are no errors, print('Method [method] valid for all provided use cases')
    """
    def __init__(self, bricks):
        """
        Stores provided values as class variables and begins testing
        """
        self.cache = self.generate_cache(bricks + 1)
        self.solution = self.get_staircases(bricks)
    
    def get_solution(self):
        return self.solution

    def generate_cache(self,n):
        cache = [[None for c in range(n)] for r in range(n)]
        return cache

    def show_2d_list(self, data):
        for d in data:
            print d

    def get_staircases(self, n):
        maximum_stair_len = int(math.floor(((8 * n + 1) ** 0.5 - 1) / 2)) #Comes from OEIS A008289
        print maximum_stair_len
        for k in range(1, int(maximum_stair_len) + 1):
            self.partition_function_q(n, k)
        print self.cache[-1][1:maximum_stair_len]
        return sum(self.cache[-1][1:maximum_stair_len])
        self.show_2d_list(self.cache)
        pass

    def partition_function_q(self, n, size):
        """
        This is the partition function Q as per the documentation in OEIS A008289. Calculates how many
        partitions exist for a number 'n' of a particular size 'size'

        Args:
        n - The integer value that must be broken into partitions
        size - the size of the partitions that will be counted
        cache - the record of previous results. The cache allows the solution to utilize dynamic programming

        Returns:
        Number of partitions of 'n' with 'size' integers
        """
        #most of this switch statement comes from the formula on OEIS A008289
        if n == size == 1:
            return 1
        elif n > 0 and size == 0:
            return 0
        elif n < size or size < 1:
            return 0
        if self.cache[n][size] == None:
            self.cache[n][size] = self.partition_function_q(n - size, size) + self.partition_function_q(n - size, size - 1)
        return self.cache[n][size]

def solution(n):
    """
    Solves problem of the staircase. Calculates the maxStairLen based on n and initiates recursion
    """
    return StaircaseSolver(n).get_solution()


print solution(200)