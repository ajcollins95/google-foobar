"""A solution to the doomsday fuel problem from google foobar.

The given problem can be modeled as an absorbing markov chain, where each empty
state is absorbing, and any non-empty states can be considered transient. This
solution manipulates a fuel array into a transition matrix in canonical form (as
per wikipedia definition). Once in this form, matrix Q and R are calculated.
We solve for F = (1-Q) ** -1 and calc FR which is a matrix of probabilities that 
various states will be reached.

Reference:
https://en.wikipedia.org/wiki/Absorbing_Markov_chain

Note: I leaned heavily on existing solutions to solve this. I have cited 
references where applicable. I hope to implement a matrix exponentiation version
of this solution when time permits.

"""

from fractions import Fraction, gcd
import copy

def solution(fuel):
    """Solves the doomsday_fuel problem from google foobar.

    Standardizes the input into a probability transition matrix. From there, 
    extracts the submatrices Q and R as per the wikipedia definition of an
    absorbing markov chain. Then Q and R can be used to get the calculate F
    and FR which will allow us to get the matrix of probabilities

    Args:
    2D Matrix of state changing probabilities

    Returns:
    1D Array containing the probabilities that each state will be reached
    The index of the return value is the probability that state index
    is reached. Effectively:
    probability_state_i = return[i]/return[-1]
    """

    #For the edge case when there is only one state
    if len(fuel) <= 1:
        return [1, 1]

    #puts fuel matrix into a probability transition matrix
    trans_fuel = fuel_to_transition(fuel)

    #Get the submatrices according to the standard matrix form
    submatrices = extract_submatrices(trans_fuel)

    Q = submatrices[0]
    R = submatrices[1]

    #Calculate F as per matrix definitions
    F = calc_f(Q)
    FR = matrix_multiply(F,R)
    ans = format_solution(FR, trans_fuel)

    return ans

def fuel_to_transition(fuel):
    """Turns an input 2D array into a more explicit absorb markov chain format.

    Each non zero element is converted from an integer to a probability, [0,1],
    that the next state will be traveresed. Absorbing state rows have a 100% (1)
    probability that they will be reached, and these are added to their rows.

    Args:
    2D Matrix of state changing probabilities

    Returns:
    2D array of float probabilities for each state to transition. 
    """

    trans_fuel = []

    for (i, row_i) in enumerate(fuel):
        row_i_sum = sum(row_i)
        if sum(row_i):
            new_row_i = [float(elem)/float(row_i_sum) for elem in row_i]
            trans_fuel.append(new_row_i)
        else:
            row_i[i] = 1
            trans_fuel.append(row_i)

    return trans_fuel

def extract_submatrices(trans_fuel):
    """Gets submatrices Q and R from the formatted transition matrix.

    Iterates through the transition matrix to get the non absorbing rows. Then,
    The individual elements oin those rows are placed into R or Q depending on 
    if they correspond to an abosrbing or non-absorbing state.

    Reference:
    https://pages.cs.wisc.edu/~shrey/2020/08/10/google-foobar.html

    Args:
    Transition Matrix from fuel_to_transition()

    Returns:
    Array of [Q,R] according to canonical form of transition matrices for AMC's  
    """
    #gets a list of absorbing rows
    absorb_rows = [i for i in range(len(trans_fuel)) if 1 == trans_fuel[i][i]]

    #loop variables
    R = []
    Q = []
    for (r, row_r) in enumerate(range(len(trans_fuel))):
        #only interested in non absorbing rows
        if not r in absorb_rows:
            r_row = []
            q_row = []
            for (c, row_c) in enumerate(range(len(trans_fuel[0]))):
                #create R and Q based on the corresponding index probabilities
                if c in absorb_rows:
                    r_row.append(trans_fuel[r][c])
                else:
                    q_row.append(trans_fuel[r][c])
            R.append(r_row)
            Q.append(q_row)
    return [Q, R]

def calc_f(Q):
    """
    Calculates F (F = (I - Q) ** -1) as per canonical form.
    """

    n = len(Q)
    return inverse_matrix(subtract_matrices(identity_matrix(n),Q))
    
def format_solution(FR, trans_fuel):
    """Turns an exponetiated input into the final formatted solution

    We only care about the top row of the exponentiated array; this represents
    the probabilities for state 0 in the original input. We then convert the
    elements of that row to fractions, and return only the elements that 
    correspond to absorbing states.

    Args:
        FR: the matrix product of F and R
        trans_fuel: the transition matrix created above
        

    Returns:
        Formatted 1D array of integers. The last index is the denominator. The 
        other elements are numerators that correspond to the probability that
        the states at those indices will be reached in the long term.

        [0, 3, 2, 9, 14]
    """
    max_32bit_int = 2147483647

    #top row describes probabilities when starting at state 0
    exp_top_row = FR[0] 

    #convert elements to fractions using max32int as max denominator
    fract_fuel = [Fraction(elem).limit_denominator(max_32bit_int)
                  for elem in exp_top_row]

    #get indices of terminal states in original input
    terminal_states = []
    for i in enumerate(range(len(trans_fuel))):
        if trans_fuel[i][i] == 1:
            terminal_states.append(i)
    
    #get denominators of the elements and their least common multiple
    denoms = [elem.denominator for elem in fract_fuel]
    lcm = get_lcm(denoms)

    #formats the data into the required syntax
    probs = [lcm]
    for i in range(len(terminal_states)):
        last = (lcm * fract_fuel.pop()).numerator
        probs.insert(0, last)

    return probs
    
    

######
#UTILS
######

def get_lcm(numbers):
    """
    Gets lcm of the array of numbers
    """
    lcm = 0
    num_last = numbers[0]
    for (i, num_i) in enumerate(range(len(numbers))):
        lcm_i = abs(num_i * num_last) // gcd(num_i, num_last)
        if lcm_i > lcm:
            lcm = lcm_i
    return lcm

def is_equal(x, y, epsilon = float(10 ** -25)):
    """
    Compares floats for equality with a default epsilon of 10 ** -25.
    """
    #compares float equality
    return abs(x-y) < epsilon

def are_matrices_equal(A,B):
    """
    Uses float equality to check all elements of two matrices for equality
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

def subtract_matrices(A, B):
    """
    Performs matrix subtraction
    """

    #confirm correct sizing
    assert len(A) == len(B) and len(A[0]) == len(B[0])

    #create 2D matrix without unwanted aliasing
    (rows, cols) = (len(A), len(A[0]))
    m_diff = [[0 for i in range(cols)] for j in range(rows)]
    assert len(m_diff) == len(A) and len(m_diff[0]) == len(A[0])

    #iterate through solution array, do the matrix subtraction math
    for r in range(rows):
        for c in range(cols):          
            A_rc = A[r][c]
            B_rc = B[r][c]
            m_diff[r][c] = A_rc - B_rc
    return m_diff

def identity_matrix(n):
    """
    Creates an identity matrix of size n
    """
    #creates identity matrix
    I = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I

def scalar_matrix_mult(M, s):
    """
    Multiplies a matrix by a scalar
    """
    #multiplies matrix by a scalar
    (rows, cols) = (len(M), len(M[0]))
    s_prod = [[s*M[j][i] for i in range(cols)] for j in range(rows)]
    return s_prod

def inverse_matrix(A):
    """Gets the inverse of a matrix A

    Uses matrix algebra to solve for the inverse of matrix A.

    Reference:
    http://integratedmlai.com/matrixinverse/

    Args:
        FR: 2D list pretending to be a matrix

    Returns:
        Inverse matrix of A
    """

    #test squareness
    assert len(A) == len(A[0])
 
    #Initialize loop variables
    n = len(A)
    AM = copy.deepcopy(A)
    I = identity_matrix(n)
    IM = copy.deepcopy(I)
 
    # Section 3: Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        diag = AM[fd][fd]
        if diag:
            fd_scalar = float(1)/float(diag)
        else:
            assert False
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fd_scalar
            IM[fd][j] *= fd_scalar
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: 
            # *** skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): 
                # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    return IM

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
