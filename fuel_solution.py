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
    fract_fuel = getSolutionMatrix(std_fuel)

    #formats into a single line answer
    results = formatSolution(fract_fuel, fuel)a
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

def mMultiply(A,B):

    #get inner dimensions, test that the matrix has corect sizing
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
#TESTS
######

def runTests():
    data = lambda:0
    data.testCases = [
        [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ],
        [
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],

        ]
    ]
    
    assert(testStandardize(data))
    print("Standardize passed Tests!")
    assert(testSolutionMatrix(data))
    #testFormatSolution()
    solution(data.testCases[1])
    pass

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
    

def testStandardize(data):
    data.answers = [
        [
            [0, .5, 0, 0, 0, .5],
            [float(4/9), 0, 0, float(3/9), float(2/9), 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]

        ],
        [
            [0, float(2/3), float(1/3), 0, 0],
            [0, 0, 0, float(3/7), float(4/7)],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],

        ]
    ]
    tests_passed = 0

    #Go through each of the test cases
    for case in range(len(data.testCases)):

        #initialize loop variables
        test = standardizeFuel(data.testCases[case])
        answer = data.answers[case]
        matches = 0
        #compare each element of the test and the answers
        for row in range(len(test)):
            for col in range(len(test[0])):
                if isEqual(test[row][col], answer[row][col]):
                    matches += 1
        if matches == len(test) * len(test[0]):
            #print(f'Standardize Test #{case} passed!')
            tests_passed += 1
    return tests_passed == len(data.testCases)


def testSolutionMatrix(data):
    '''
    data.answers = [
        [
            [0, .5, 0, 0, 0, .5],
            [float(4/9), 0, 0, float(3/9), float(2/9), 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]

        ],
        [
            [0, float(2/3), float(1/3), 0, 0],
            [0, 0, 0, float(3/7), float(4/7)],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],

        ]
    ]
    '''
    data.multCases = [
        (
            [
                [10,20,10],
                [4,5,6],
                [2,3,5]
            ],
            [
                [3,2,4],
                [3,3,9],
                [4,4,2]
            ]
        ),
        (
            [
                [5,8],
                [3,8]
            ],
            [
                [3,8],
                [8,9],
            ]
        ),
        (
            [
                [5,7,9,10],
                [2,3,3,8],
                [8,10,2,3],
                [3,3,4,8]
            ],
            [
                [3,10,12,18],
                [12,1,4,9],
                [9,10,12,2],
                [3,12,4,10]
            ]
        ),
        (
            [
                [10,20,10],
                [4,5,6],
                [2,3,5]
            ],
            [
                [10,20,10],
                [4,5,6],
                [2,3,5]
            ],
        )

        
    ]
    data.multAnswers = [
        [
            [130,120,240],
            [51,47,73],
            [35,33,45]
        ],
        [
            [79,112],
            [73,96]
        ],
        [
            [210,267,236,271],
            [93,149,104,149],
            [171,146,172,268],
            [105,169,128,169]
        ],
        [
            [200,330,270],
            [72,123,100],
            [42,70,63]
        ]
        
    ]
    data.solAnswers = []
    test_areMatricesEqual(data)
    print('areMatricesEqual() passed tests!')
    test_mMultiply(data)
    print('mMultiply(data) passed tests!')
    for case in data.testCases:
        #print("\n")
        std_fuel = standardizeFuel(case)
        sol_fuel = getSolutionMatrix(std_fuel)
        for elem in sol_fuel:
            pass
            #print (Fraction(elem).limit_denominator(2147483647))
    #test_exponentiateMatrix(data)
    #print('exponentiateMatrix(data) passed tests!')

    

    tests_passed = 0
    return True

def test_mMultiply(data):
    matches = 0
    for case in range(len(data.multAnswers)):
        assert len(data.multCases) == len(data.multAnswers)
        A = data.multCases[case][0]
        B = data.multCases[case][1]
        prod = mMultiply(A,B)
        assert areMatricesEqual(prod, data.multAnswers[case])
        #print(f'mMultiply Case #{case} passed test...')
        matches += 1
    return matches == len(data.multAnswers)

def test_areMatricesEqual(data):
    data.eqCases = [
        (
            [
                [10,20,10],
                [4,5,6],
                [2,3,5]
            ],
            1
        ),
        (
            [
                [10,20,10],
                [4,5,6],
                [2,3,5]
            ],
            2
        ),
        (
            [
                [10,20,10],
                [4,5,6],
                [2,3,5]
            ],
            3
        )
        

        
    ]
    
    data.eqAnswers = [
        [
            [10,20,10],
            [4,5,6],
            [2,3,5]
        ],
        [
            [200,330,270],
            [72,123,100],
            [42,70,63]
        ],
        [
            [3860, 6460, 5330],
            [1412, 2355, 1958],
            [826, 1379, 1155]
        ]
        
    ]
    for ans in data.eqAnswers:
        assert areMatricesEqual(ans, ans)
        #print(f'test areMatricesEqual() passed!')
    assert not areMatricesEqual([[2]],[[2,3]])
    return True

def test_exponentiateMatrix(data):
    data.expCases = [
        (
            [
                [10,20,10],
                [4,5,6],
                [2,3,5]
            ],
            1
        ),
        (
            [
                [10,20,10],
                [4,5,6],
                [2,3,5]
            ],
            2
        ),
        (
            [
                [10,20,10],
                [4,5,6],
                [2,3,5]
            ],
            3
        )
        

        
    ]
    
    data.expAnswers = [
        [
            [10,20,10],
            [4,5,6],
            [2,3,5]
        ],
        [
            [200,330,270],
            [72,123,100],
            [42,70,63]
        ],
        [
            [3860, 6460, 5330],
            [1412, 2355, 1958],
            [826, 1379, 1155]
        ]
        
    ]
    for i in range(len(data.multAnswers)):
        M = data.expCases[i][0]
        k = data.expCases[i][1]
        m_to_k = exponentiateMatrix(M,k)
        ans = data.expAnswers[i]
        assert areMatricesEqual(m_to_k, ans)
        print(f'test exponentiateMatrix() passed...')
    assert not areMatricesEqual([[2]],[[2,3]])
    return True
    
    
    
    
    
runTests()
    
