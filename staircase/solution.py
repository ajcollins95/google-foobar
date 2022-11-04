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

def g(x):
    pass

