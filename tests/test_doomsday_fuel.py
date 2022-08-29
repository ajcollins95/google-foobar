import sys

sys.path.insert(0, '/home/ajcollins/Documents/google-foobar/doomsday-fuel/solution')

from fuel_solution import *
from fuel_numpy import solution_fuel

#Declare global test cases
TEST_CASES = [
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

def areMatricesEqual(A,B):
    #tests if two 2D matrices are equivalent

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

def test_standardize():
    answers = [
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
    #initialize test variable
    tests_passed = 0

    #Go through each of the test cases
    for case in range(len(TEST_CASES)):

        #initialize loop variables
        test = standardize_fuel(TEST_CASES[case])
        answer = answers[case]
        matches = 0

        #compare each element of the test and the answers
        for row in range(len(test)):
            for col in range(len(test[0])):
                if is_equal(test[row][col], answer[row][col]):
                    matches += 1
        if matches == len(test) * len(test[0]):
            #print(f'Standardize Test #{case} passed!')
            tests_passed += 1
    return tests_passed == len(TEST_CASES)

#Test Solution Matrix

def test_areMatricesEqual():
    for case in TEST_CASES:
        assert areMatricesEqual(case, case)
    assert not areMatricesEqual([[2]], [[1]])
    assert not areMatricesEqual([[2]], [[1,4]])

def test_mMultiply():
    multCases = [
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
    multAnswers = [
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
        
    matches = 0
    for case in range(len(multAnswers)):
        assert len(multCases) == len(multAnswers)
        A = multCases[case][0]
        B = multCases[case][1]
        prod = matrix_multiply(A,B)
        assert areMatricesEqual(prod, multAnswers[case])
        #print(f'atrix_m Case #{case} passed test...')
        matches += 1
    return matches == len(multAnswers)

def test_solution():
    answers = [
        [0, 3, 2, 9 ,14],
        [7, 6, 8, 21]
    ]
    for case_i in range(len(TEST_CASES)):
        inp = TEST_CASES[case_i]
        sol_inp = solution(inp)
        ans = answers[case_i]
        assert (len(sol_inp) == len(ans))
        matches = 0
        for i in range(len(ans)):
            if sol_inp[i] == ans[i]:
                matches += 1
        assert(matches == len(ans))


def test_solutions():
    m = [
        [0,2,3,0,1],
        [0,0,0,0,0],
        [1,0,0,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    np = solution_fuel(m)
    sol = solution(m)
    disp = f'Comparison: \nnumpy: {np} \nsolution: {sol}'
    print(disp)
    return
    tests = 100
    for t in range(tests):
        pass
        #m = generate_fuel_array()
    

def test_import():
    assert(is_equal(1,1))

test_solutions()