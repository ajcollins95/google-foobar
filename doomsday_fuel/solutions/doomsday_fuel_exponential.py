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


from fractions import Fraction, gcd

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
    std_fuel = standardize_fuel(fuel)

    #uses matrix exponentiation to calculate limit as elements go to infinity
    exp_fuel = get_solution_matrix(std_fuel)

    #formats into a single line answer
    results = format_solution(exp_fuel, std_fuel)
    return results



def standardize_fuel(fuel):
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
        if sum(row_i):
            new_row_i = [float(elem)/row_i_sum for elem in row_i]
            std_fuel.append(new_row_i)
        else:
            row_i[i] = 1
            std_fuel.append(row_i)

    return std_fuel


def get_solution_matrix(std_fuel):
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
    is_steady_state = False #TODO develop better condition for steady-state limit
    kth_power = 2
    exp_fuel = std_fuel

    while(not is_steady_state):
        #Exponetiates the matrix until it reaches steady state
        is_steady_state = are_matrices_equal(
            matrix_multiply(exp_fuel, std_fuel),
            exp_fuel)
        exp_fuel = matrix_multiply(exp_fuel, std_fuel)

        kth_power += 1
    return exp_fuel
            
def format_solution(exp_fuel, std_fuel):
    """Turns an exponetiated input into the final formatted solution

    We only care about the top row of the exponentiated array; this represents
    the probabilities for state 0 in the original input. We then convert the
    elements of that row to fractions

    Args:
        exp_fuel: The exponentiated limit array as per get_solution_matrix()
        og_fuel: The original input to solution()
        

    Returns:
        Formatted 1D array of integers. The last index is the denominator. The 
        other elements are numerators that correspond to the probability that
        the states at those indices will be reached in the long term.

        [0, 3, 2, 9, 14]
    """
    max_32bit_int = 2147483647

    #top row describes probabilities when starting at state 0
    exp_top_row = exp_fuel[0] 

    #convert elements to fractions using max32int as max denominator
    fract_fuel = [Fraction(elem).limit_denominator(max_32bit_int)
                  for elem in exp_top_row]

    #get indices of terminal states in original input
    terminal_states = []
    for i in range(len(std_fuel)):
        if std_fuel[i][i] == 1:
            terminal_states.append(i)

    #find least common multiple for the fractions in the array
    denoms = [int(elem.denominator) for elem in fract_fuel]
    lcm = get_lcm(denoms) 

    probs = []
    for state in terminal_states:
        frac = fract_fuel[state]
        factor = lcm / frac.denominator
        numerator = fract_fuel[state].numerator * factor
        probs.append(numerator)
    probs.append(lcm)
    return probs
    
######
#UTILS
######

def is_equal(x, y, epsilon = float(10 ** -25)):
    """
    Compares float values for equality using a default epsilon value of 10 ** -25
    """
    return abs(x-y) < epsilon

def get_lcm(nums):
    """
    Gets the least common multiple of a list of numbers
    """
    lcm = 1
    for num in nums:
        lcm = lcm * num // gcd(lcm, num)
    return lcm

def are_matrices_equal(A,B):
    """
    Tests if two 2D matrices are equivalent
    """

    #check matrix sizing
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    #check each element is equal
    matches = 0
    for row in range(len(A)):
            for col in range(len(A[0])):
                if is_equal(A[row][col], B[row][col]):
                    matches += 1

    return matches == len(A) * len(A[0])

def matrix_multiply(A,B):
    """
    Performs matrix multiplication on two matrices
    """

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

