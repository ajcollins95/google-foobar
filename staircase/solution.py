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
        
        




