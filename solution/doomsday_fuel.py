"""A solution to the doomsday fuel problem from google foobar.

The given problem can be modeled as an absorbing markov chain, where each empty
state is absorbing, and any non-empty states can be considered transient. This
solution manipulates a fuel array into a transition matrix in canonical form (as
per wikipedia definition). Once in this form, matrix Q and R are calculated.
We solve for FR

"""

from fractions import Fraction, gcd
import math

MAX_32BIT_INT = 2147483647

def solution(fuel):
    """Solves the doomsday_fuel problem from google foobar.

    Standardizes the input into a probability transition matrix. [MORE]

    Args:
    2D Matrix of state changing probabilities

    Returns:
    1D Array containing the probabilities that each state will be reached
    The index of the return value is the probability that state index
    is reached. Effectively:
    probability_state_i = return[i]/return[-1]
    """
    #print("ORIGINAL",fuel)
    if len(fuel) <= 1:
        return [1, 1]

    #puts fuel matrix into a probability transition matrix
    trans_fuel = fuel_to_transition(fuel)

    #print('precheck', trans_fuel[0][0])
    if trans_fuel[0][0] == 1:
        ans = [0]*len(fuel)
        ans[-1] = 1
        return ans



    #re_fuel = reorder_fuel(prob_fuel)
    submatrices = extract_submatrices(trans_fuel)
    Q = submatrices[0]
    R = submatrices[1]

    #Calculate F as per matrix definitions
    F = calc_f(Q)
    FR = matrix_multiply(F,R)
    ans = format_solution(FR, trans_fuel)
    #print(,ans)

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
    for i in range(len(fuel)):
        row_i = fuel[i]
        row_i_sum = sum(row_i)
        if sum(row_i):
            new_row_i = [float(elem)/row_i_sum for elem in row_i]
            trans_fuel.append(new_row_i)
        else:
            row_i[i] = 1
            trans_fuel.append(row_i)

    return trans_fuel

def extract_submatrices(trans_fuel):
    #Full transparency I did lift this from URL
    absorb_rows = [i for i in range(len(trans_fuel)) if 1 in trans_fuel[i]]
    R = []
    Q = []
    for r in range(len(trans_fuel)):
        if not r in absorb_rows:
            r_row = []
            q_row = []
            for c in range(len(trans_fuel[0])):
                if c in absorb_rows:
                    r_row.append(trans_fuel[r][c])
                else:
                    q_row.append(trans_fuel[r][c])
            R.append(r_row)
            Q.append(q_row)
    #print(Q,R)
    return [Q, R]

def calc_f(Q):
    n = len(Q)
    return inverse_matrix(subtract_matrices(identity_matrix(n),Q))
    
def format_solution(exp_fuel, og_fuel):
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
    terminal_states = set()
    for i in range(len(og_fuel)):
        #row_i = og_fuel[i]
        
        #if sum(row_i) == 1:
        if og_fuel[i][i] == 1:
            terminal_states.add(i)
    print(exp_fuel[0], terminal_states)

    #find least common multiple for the fractions in the array
    denoms = [elem.denominator for elem in fract_fuel]

    lcm = get_lcm(denoms) #2.7 implementation
    #lcm = math.lcm(*denoms) #python 3 implementation

    probs = [lcm]
    for i in range(len(terminal_states)):
        last = (lcm * fract_fuel.pop()).numerator
        probs.insert(0, last)
    return probs

######
#UTILS
######

def get_lcm(numbers):
    #gets lcm of the array of numbers
    lcm = 0
    num_last = numbers[0]
    for i in range(len(numbers)):
        num_i = numbers[i]
        lcm_i = abs(num_i * num_last) // gcd(num_i, num_last)
        if lcm_i > lcm:
            lcm = lcm_i
    return lcm

def is_equal(x, y, epsilon = float(10 ** -25)):
    #compares float equality
    return abs(x-y) < epsilon

def are_matrices_equal(A,B):
    #tests if two 2D matrices are equivalent

    #check matrix sizing
    print(A,B)
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
    #performs matrix subtraction

    #confirm correct sizing
    assert len(A) == len(B) and len(A[0]) == len(B[0])

    #create 2D matrix without unwanted aliasing
    (rows, cols) = (len(A), len(A[0]))
    m_diff = [[0 for i in range(cols)] for j in range(rows)]
    assert len(m_diff) == len(A) and len(m_diff[0]) == len(A[0])

    #iterate through solution array, do the matrix product math
    for r in range(rows):
        for c in range(cols):          
            A_rc = A[r][c]
            B_rc = B[r][c]
            m_diff[r][c] = A_rc - B_rc
    return m_diff

def identity_matrix(n):
    #creates identity matrix
    I = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I

def scalar_matrix_mult(M, s):
    (rows, cols) = (len(M), len(M[0]))
    s_prod = [[s*M[j][i] for i in range(cols)] for j in range(rows)]
    return s_prod

def copy_matrix(M):
    (rows, cols) = (len(M), len(M[0]))
    copy = [[M[j][i] for i in range(cols)] for j in range(rows)]
    return copy

def inverse_matrix(A):
    #stole this too

    #test squareness
    assert len(A) == len(A[0])
 
    #Initialize loop variables
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)
 
    # Section 3: Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        diag = AM[fd][fd]
        if diag:
            #fdScaler = Fraction(1,diag).limit_denominator(MAX_32BIT_INT)
            fdScaler = 1.0/diag
        else:
            assert False
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
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
    #performs matrix multiplication on two matrices

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

unterminated = [
    [0,0,0,0,0],
    [1,2,0,4,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]


#print ("un",solution(unterminated))