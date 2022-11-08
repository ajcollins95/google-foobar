import sys
import timeit
import math
from solution import *

class StaircaseSolver:
    """
    A python class that solves the grandest-staircase problem

    My solution to the grandest-staircase problem uses (amongst other things)
    recursion, numerical partitioning, and dynamic programming. 

    In the implementation of dynamic programming, I needed to come up with a way to
    implement a memo/cache to store previously caclulated values. I chose to use a class 
    to solve this problem because I wanted to use a cache variable, but I didn't want 
    the cache to be completely global. In this class I have implemented the cache as
    an instance variable, which is a simple workaround.

    Attributes
    cache: an implementation of a memo to enable the storage of computed values
    solution: the answer to the grandest-staircase problem where bricks = n
    """
    def __init__(self, bricks):
        """Inits the class with the provided number of bricks"""
        self.cache = self.generate_cache(bricks + 1)
        self.solution = self.get_staircases(bricks)
    
    def get_solution(self):
        """Public getter so that the solution can be returned outside of the class"""
        return self.solution

    def generate_cache(self, n):
        """
        Generates a cache of None-type values to act as a ledger for computed values

        Args:
        n - size (n x n) of the cache

        Returns
        An n x n List of None-types

        """
        cache = [[None for c in range(n)] for r in range(n)]
        return cache

    def show_2d_list(self, data, maximum_stair_len):
        for i in range(3, len(data)):
            #print (i, sum(data[i][1:maximum_stair_len]))
            #print (i, data[i])
            print (i, self.get_row_sum(data[i]))

    def get_row_sum(self, row):
        """
        Gets the sum of a row of the cache.

        Some of the rows have different amounts of None-types in them. This is a naive
        way to sum only the integer values of a row.

        Args:
        row - a List of integers and None-types from the cache instance variable

        Returns:
        The sum of the integers in the given row
        """
        running_sum = 0
        for i in range(2,len(row)): # start at 2 because that's the min number of stairs
            if row[i] != None:
                running_sum += row[i]
            else:
                return running_sum


    def get_staircases(self, n):
        """
        Given a number of bricks n, this calculates the number of staircases that can be made.

        Iterates through all possible n values and numbers of stairs. Run the recursive distinct 
        partition function to build out the cache of distinct partitions at Q(n, k) as per the 
        formula in OEIS A008289

        Args:
        n - number of bricks in staircase

        Returns:
        Number of possible stairase combinations with n bricks
        """
        maximum_stair_len = int(math.floor(((8 * n + 1) ** 0.5 - 1) / 2)) #Comes from OEIS A008289, max triangle number less than n
        for n in range(1, n + 1):
            for stairs in range(1, int(maximum_stair_len) + 1):
                self.partition_function_q(n, stairs)

        return self.get_row_sum(self.cache[-1])

    def partition_function_q(self, n, size):
        """
        This is the partition function Q as per the documentation in OEIS A008289. Calculates how many
        partitions exist for a number 'n' of a particular size 'size'. Updates the cache so that previously
        calculated values can be used instead of having to calculate the smae values multiple times.

        Args:
        n - The integer value that must be broken into partitions
        size - the size of the partitions that will be counted

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


