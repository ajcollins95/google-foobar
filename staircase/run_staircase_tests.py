import sys
from solution import *

class Test:
    """
    A class for helping facilitate testing. Takes a list of tuples and a method.
    Tests that the use cases evaluate properly on the provided method

    Args
    method - the method from solution.py that is being tested against the use cases
    use_cases - a list of tuples where tuple[1] is the expected result of method(tuple[0])
    (ie, tuple = (method_input, output))

    Returns
    Nothing. If there is an assertion error, print the input, expected result, and actual result.
    If there are no errors, print('Method [method] valid for all provided use cases')
    """
    def __init__(self, method, use_cases, input_fields = 1):
        """
        Stores provided values as class variables and begins testing
        """
        self.use_cases = use_cases
        self.method = method
        self.input_fields = input_fields
        self.test_method()

    def handle_input(self, use_case_input):
        """
        This turns the use case input into a list which can then
        be unpacked by test_method()
        """
        if self.input_fields == 1:
            return [use_case_input]
        elif self.input_fields < 1:
            assert False
            return 'fml'
        else:
            assert isinstance(use_case_input, list)
            return use_case_input
        


    def test_method(self):
        """
        Runs the use cases against the provided method
        """
        for i, use_case in enumerate(self.use_cases):
            method_input = self.handle_input(use_case[0])
            output = use_case[1]
            method_return = self.method(*method_input)
            try:
                assert method_return == output
            except AssertionError:
                print("Method '{_method}' failed when input was {_method_input}".format(
                    _method = self.method.__name__,
                    _method_input = method_input)
                    )
                print('Expected: {_output}'.format(_output = output))
                print('Method returned: {_method_return}'.format(_method_return = method_return))
                assert False
        print("Method '{_method}' passed all provided use cases...".format(_method = self.method.__name__))
        
    

def run():
    """
    Runs all the tests for the staircase problem. Test failures
    will result in a failed assert statement.
    """
    is_correct_version()
    test_get_minimum_tail_sum()
    test_get_max_stairs()
    test_is_valid_staircase()
    test_get_triangular_tail()
    test_combinations_at_staircase_length()
    test_solution()

    print("All test methods in run() have passed!")

def is_correct_version():
    """
    make sure this is running in the 2.7 sandbox
    """
    pyVersion = sys.version_info
    #print("PY VERSION", pyVersion.major, type(pyVersion))

    assert(pyVersion.major == 2 and pyVersion.minor == 7)



def test_get_minimum_tail_sum():
    """
    Tests gMTS() against use cases
    """
    use_cases = [
        (0, 0),
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
        (6, 21),
        (7, 28),
        (10, 55),
        (18, 171),
        (19, 190),
        (20, 210)
    ]
    Test(get_minimum_tail_sum, use_cases)

def test_get_max_stairs():
    use_cases = [
        (3, 2),
        (4, 2),
        (5, 2),
        (6, 3),
        (7, 3),
        (8, 3),
        (9, 3),
        (10, 4),
        (11, 4),
        (12, 4),
        (13, 4),
        (14, 4),
        (15, 5),
        (54, 9),
        (55, 10),
        (56, 10),
        (199, 19),
        (200, 19),
    ]
    Test(get_max_stairs, use_cases)

def test_is_valid_staircase():
    use_cases = [
        ([[3,2,1], 6], True),
        ([[3,2,1], 7], False),
        ([[2, 1], 3], True),
        ([[3, 1], 4], True),
        ([[7,2,1], 10], True),
        ([[6,3,1], 10], True),
        ([[7,2,2], 11], False),
        (['bingo',10], False),
        ([[7,2.3,1],10], False),
        ([[5,3,2,1],11], True),
        ([[5,3,2,2],12], False),
    ]
    Test(is_valid_staircase, use_cases, input_fields=2)

def test_get_triangular_tail():
    use_cases = [
        ([6, 2, 5], [1]),
        ([6, 3, 3], [2, 1]),
        ([10, 4, 4], [3, 2, 1]),
        ([15, 4, 9], [3, 2, 1]),
        ([15, 5, 5], [4, 3, 2, 1]),
    ]
    Test(get_triangular_tail, use_cases, input_fields=3)

def test_combinations_at_staircase_length():
    use_cases = [
        ([5, 2], [[4, 1], [3, 2]]),
        ([10, 2], [[9, 1], [8, 2], [7, 3], [6, 4]]),
        ([14, 2], [[13, 1], [12, 2], [11, 3], [10, 4], [9, 5], [8, 6]]),
        ([6, 3], [[3, 2, 1]]),
        ([11, 3], [[8, 2, 1], [7, 3, 1], [6, 4, 1], [6, 3, 2], [5, 4, 2]]),
        ([10, 4], [[4, 3, 2, 1]]),
        ([14, 4], [[8, 3, 2, 1], [7, 4, 2, 1], [6, 5, 2, 1], [6, 4, 3, 1], [5, 4, 3, 2], ]),
        
    ]
    Test(combinations_at_staircase_length, use_cases, input_fields=2)

def test_solution():
    use_cases = [
        (3, 1),
        (4, 1),
        (5, 2),
        (6, 3),
        (7, 4),
        (8, 5),
        (9, 7),
        (10, 9),
        (11, 11),
        (12, 14),
        (13, 17),
        (14, 21),
        (15, 26),
        (200, 487067745)
    ]
    Test(solution, use_cases)

run()