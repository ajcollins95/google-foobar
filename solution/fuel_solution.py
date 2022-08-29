from fractions import Fraction
import math

def solution(fuel):
    """
    Adhere to style guide!!!
    stuff
    """
    if len(fuel) <= 1:
        return [1, 1]

    #puts fuel matrix into standard form with probabilities
    std_fuel = standardizeFuel(fuel)

    #uses matrix exponentiaition to calculate limit as each element goes to infinity
    #returns top row of limit matrix 
    fract_fuel = getSolutionMatrix(std_fuel)

    #formats into a single line answer
    results = formatSolution(fract_fuel, fuel)
    return results

def standardizeFuel(fuel):
    """
"""
    std_fuel = []
    for i in range(len(fuel)):
        row_i = fuel[i]
        row_i_sum = sum(row_i)
        if sum(row_i) == 0:
            row_i[i] = 1
            std_fuel.append(row_i)
        else:
            new_row_i = [float(elem)/row_i_sum for elem in row_i]
            std_fuel.append(new_row_i)
    return std_fuel


def getSolutionMatrix(std_fuel):
    isTopLeftZero = False
    max_32bit_int = 2147483647
    kth_power = 2
    exp_fuel = std_fuel
    precision = 15 #Eventually not a magic number
    epsilon = 10 ** -precision
    while(not isTopLeftZero):
        exp_fuel = mMultiply(exp_fuel, std_fuel)
        isTopLeftZero = isEqual(exp_fuel[0][0],0, epsilon) and isEqual(exp_fuel[1][0],0, epsilon)
        kth_power += 1
    fract_fuel = [Fraction(elem).limit_denominator(max_32bit_int) for elem in exp_fuel[0]]
  
    return fract_fuel
            
def formatSolution(sol_fuel, og_fuel):
    terminal_states = set()
    for i in range(len(og_fuel)):
        row_i = og_fuel[i]
        print(sum(row_i))
        if sum(row_i) == 1:
            terminal_states.add(i)
    denoms = [elem.denominator for elem in sol_fuel]
    lcm = math.lcm(*denoms)
    probs = [lcm]
    print(len(terminal_states))
    for i in range(len(terminal_states)):
        print('a')
        last = (lcm * sol_fuel.pop()).numerator
        print(last)
        probs.insert(0, last)
    print(probs)
    return probs

######
#UTILS
######

def isEqual(x, y, epsilon = float((100 * 2147483647) ** -1)):
    #compares float equality
    #epsilon is max 32 bit int

    return abs(x-y) < epsilon

def areMatricesEqual(A,B):
    #check matrix sizing
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    #check each element is equal
    matches = 0
    for row in range(len(A)):
            for col in range(len(A[0])):
                if isEqual(A[row][col], B[row][col]):
                    matches += 1

    return matches == len(A) * len(A[0])

def mMultiply(A,B):

    #get inner dimensions, test that the matrix has correct sizing
    inner_dimens = (len(A[0]), len(B))
    assert inner_dimens[0] == inner_dimens[1]

    #get the outer dimensions of the solution
    m_dimens = (len(A), len(B[0]))
    (rows, cols) = (m_dimens[0], m_dimens[1])

    #create 2D matrix without unwanted aliasing
    m_prod = [[0 for i in range(cols)] for j in range(rows)]
    assert len(m_prod) == m_dimens[0] and len(m_prod[0]) == m_dimens[1]

    #iterate through solution array, do the matrix product math
    for m_row in range(m_dimens[0]):
        for m_col in range(m_dimens[1]):
            elem_sum = 0
            for i in range(inner_dimens[0]):
                elem_sum += A[m_row][i] * B[i][m_col]
            m_prod[m_row][m_col] = elem_sum
    return m_prod