"""A solution to the doomsday fuel problem from google foobar.

The given problem can be modeled as an absorbing markov chain, where each empty
state is absorbing, and any non-empty states can be considered transient. This 
solution uses matrix exponentiation to approximate the limit of each input 
element.

Limit (M ** k)
as k -> inf

where:
M = input matrix
k = variable exponent

As k increases, many values will approach zero. At this point, the matrix of
limits is a matrix of probabilities that each state will be reached over time.

"""


from fractions import Fraction
import math

def solution(fuel):
    """Solves the doomsday_fuel problem from google foobar.

    Standardizes the input into something that can be exponentiated correctly.
    Exponentiates the above until the top left corner is appx. zero.
    Formats result into [prob_i prob_i prob_i denom]

    Args:
    2D Matrix of state changing probabilities

    Returns:
    1D Array containing the probabilities that each state will be reached
    The index of the return value is the probability that state index
    is reached. Effectively:
    probability_state_i = return[i]/return[-1]
    
    """
    if len(fuel) <= 1:
        return [1, 1]

    #puts fuel matrix into standard form with probabilities
    std_fuel = standardizeFuel(fuel)

    #uses matrix exponentiation to calculate limit as elements go to infinity
    #returns top row of limit matrix 
    fract_fuel = getSolutionMatrix(std_fuel)

    #formats into a single line answer
    results = formatSolution(fract_fuel, fuel)
    return results

def standardizeFuel(fuel):
    """Turns an input 2D array into a more explicit absorb markov chain format.

    Each non zero element is converted from an integer to a probability, [0,1],
    that the next state will be traveresed. Absorbing state rows have a 100% (1)
    probability that they will be reached, and these are added to their rows.

    Args:
    2D Matrix of state changing probabilities

    Returns:
    2D array of float probabilities for each state to transition.   
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
    """Turns a formatted fuel array into the exponentiated limit -> infinity.

    Define f(x) = M ** k. As Lim f(x) approaches infinity, the resulting 
    matrix will be the probabilities that each state will be reached in the
    long term. We know that the top left values will approach zero, so we stop 
    exponentiating when the zero values reach a suitable epsilon. This is 
    the condition for the "limit"

    Args:
    2D Matrix of formatted state probabilities

    Returns:
    2D array of float probabilities for each state to transition.   
    """
    isTopLeftZero = False
    max_32bit_int = 2147483647
    kth_power = 2
    exp_fuel = std_fuel
    precision = 15 #Eventually not a magic number
    epsilon = 10 ** -precision
    while(not isTopLeftZero):
        exp_fuel = mMultiply(exp_fuel, std_fuel)
        isTopLeftZero = (isEqual(exp_fuel[0][0],0, epsilon) and
                         isEqual(exp_fuel[1][0],0, epsilon))
        kth_power += 1
    fract_fuel = [Fraction(elem).limit_denominator(max_32bit_int)
                  for elem in exp_fuel[0]]
  
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