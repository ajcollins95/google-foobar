from doomsday_fuel import *
#from fuel_numpy import solution_fuel

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
def test_solution():
    for case in range(len(TEST_CASES)):
        print(solution(TEST_CASES[case]))

def run_tests():
    test_sol_functions()
    test_solution()

def test_sol_functions():
    test_fuel_to_transition()
    test_extract_submatrices()
    test_subtract_matrices()
    test_scalar_matrix_mult()
    test_copy_matrix()
    test_inverse_matrix()


def test_fuel_to_transition():
    answers = [
        [
            [0, .5, 0, 0, 0, .5],
            [float(4)/9, 0, 0, float(3)/9, float(2)/9, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]

        ],
        [
            [0, float(2)/3, float(1)/3, 0, 0],
            [0, 0, 0, float(3)/7, float(4)/7],
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
        test = fuel_to_transition(TEST_CASES[case])
        
        answer = answers[case]
        matches = 0

        #compare each element of the test and the answers
        for row in range(len(test)):
            for col in range(len(test[0])):
                if is_equal(test[row][col], answer[row][col]):
                    matches += 1
        if matches == len(test) * len(test[0]):
            #print(f'Standardize Test #{case} passed!')
            print(case)
            tests_passed += 1
    assert tests_passed == len(TEST_CASES)

def test_extract_submatrices():
    tests = [
        [
            [1,0,0,0],
            [.1,.8,.1,0],
            [.1,.4,.4,.1],
            [0,0,0,1]
        ]

    ]

    answers = [
        [
            [
                1
            ],
            [
                1
            ]
        ]
    ]

    extract_submatrices(tests[0])

def test_subtract_matrices():
    tests = [
        (
            [
                [4,16],
                [10,22],
            ],
            [
                [1,15],
                [6,3],
            ]
        ),
        (
            [
                [2,8],
                [0,9]
            ],
            [
                [5,6],
                [11,3],
            ]
        ),
        (
            [
                [3,4,9],
                [6,8,6],
                [7,3,4]
            ],
            [
                [1,6,7],
                [6,4,2],
                [4,1,5]
            ],
        )
    ]
    answers = [
        [   
            [3,1],
            [4,19]
        ],
        [
            [-3,2],
            [-11,6],
        ],
        [
            [2, -2, 2], 
            [0, 4, 4], 
            [3, 2, -1]
        ]
    ]
    for case in range(len(answers)):
        assert subtract_matrices(tests[case][0],tests[case][1]) == answers[case]

def test_scalar_matrix_mult():
    pass
    tests = [
        (
            [
                [1,1,1],
                [1,1,1],
                [1,1,1]
            ],
            Fraction(1,4)
        )
    ]
    #print scalar_matrix_mult(tests[0][0], tests[0][1])

def test_copy_matrix():
    tests = [
        [
            [3,5,7],
            [5,7,9],
            [8,9,9]

        ],
        [
            [2,3,4],
            [1,2,3],
            [1,1,0]
        ],
        [
            [6,2,3],
            [0,0,4],
            [2,0,0]
        ]
    ]
    for test in tests:
        assert are_matrices_equal(test, copy_matrix(test))

def test_inverse_matrix():
    tests = [
        [
            [3,5,7],
            [5,7,9],
            [8,9,9]

        ],
        [
            [2,3,4],
            [1,2,3],
            [1,1,0]
        ]
    ]
    answers = [
        [
            [-4.5,4.5,-1],
            [6.75,-7.25,2],
            [-2.75,3.25,-1]

        ],
        [
            [3,-4,-1],
            [-3,4,2],
            [1,-1,-1]
        ]

    ]
    M = [
        [5,3,1],
        [3,9,4],
        [1,3,5]
    ]
    #print(inverse_matrix(M))
    #assert False
    for case in range(len(tests)):
        #print(inverse_matrix(tests[case]))
        #print(answers[case])
        assert are_matrices_equal(inverse_matrix(tests[case]),answers[case])
    assert False

#run_tests()
