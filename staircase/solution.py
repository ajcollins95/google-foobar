def solution(n):
    pass

def get_max_stairs(b):
    """This method calculates the longest staircase that b bricks will be able to build

    Takes a number of bricks and determines what the maximum length of the staircase can
    be. This is based on triangular numbers; if triNum(n) <= b < triNum(n+1), maxLen = n

    Args:
    b - b is the integer that represents the provided number of bricks

    Returns:
    The integer representing the number of stairs in the longest staircase that b bricks
    can build.
    """
    assert b >= 3 #based on parameters of the problem statement
    triangle_base = 2
    exit_condition = (get_minimum_tail_sum(triangle_base) <= b and
            b < get_minimum_tail_sum(triangle_base + 1))
    while(not exit_condition and triangle_base < 20):
        triangle_base += 1
        exit_condition = (get_minimum_tail_sum(triangle_base) <= b and
            b < get_minimum_tail_sum(triangle_base + 1))
    return triangle_base

def combinations_at_staircase_length():
    pass
        
def get_minimum_tail_sum(n):
    """Gets the smallest sum for a staircase with n stairs

    Takes a stair length and determines the sum of the smallest staircase
    values that are possible in a size n staircase. It turns out that this
    is essentially just finding the 'triangular number' of base n.

    Args:
    n = integer length of the staircase in question

    Returns:
    Integer - the smallest sum possible for staircase length n. This is achieved
    by calculating the pyramid number of base n. The forumla for triangular numbers
    is n(n+1)/2.
    """
    return n *(n + 1) / 2

def get_tail():
    pass

def is_valid_staircase(s, b):
    """
    Determines if the given input is actually formatted correctly, and is valid based
    on challenge prompt and given number of bricks.

    Args:
    s - a list of integers that represents the height of bricks in a staircase
    b - an integer representing the total number of bricks

    Returns
    Boolean value representing whether or not the staircase 's' is valid based
    on the definition in the challenge prompt.
    """
    if (not type(s) == 'list' or
        sum(s) != b):
        return False
    elif (not all(isinstance(item, int) for item in s)):
        return False
    else:
        #no explicit testing for correct length, testing sum and descending order should be
        #sufficient. Can tease this assumption out in testing
        i = 1 #start at index 1 because we know that there are always at least two stairs
        is_stair_i_smaller = s[i-1] > s[i]
        while is_stair_i_smaller:
            if i + 1 == len(s):
                return True
            i += 1
            is_stair_i_smaller = s[i-1] > s[i]
        return False










