import sys
import timeit
from solution import *

def solution_alpha(n):
    #another implementation with dynamic programming
    comboRef = [[-1],[-1],[-1]]
    for b in range(3, n + 1):
        maxStairs = get_max_stairs(b)
        comboRef.append([-1] * (maxStairs + 1))

        for s in range(2, maxStairs + 1):
            if s == 2:
                print(b,s)
                comboRef[b][s] = (b - 1) / 2 #formula for number of pairings
            else:
                combinationsAtStaircaseLength(b, s, comboRef)
    showComboRef(comboRef)
    return sum(comboRef[n][2:])

def combinationsAtStaircaseLength(b, s, comboRef):
    #recursive function to calculate cominations at lengths
    minTailSum = get_minimum_tail_sum(s-1) #3
    combos = 0
    for tailSum in range(minTailSum, b):
        head = b - tailSum
        if head > tailSum:
            #comboRef[b][s] = comboRef[tailSum][s-1]
            combos += comboRef[tailSum][s-1]
        elif head == tailSum:
            
    comboRef[b][s] = combos

def showComboRef(comboRef):
    for i in range(len(comboRef)):
        print(i, comboRef[i])

solution_alpha(10)