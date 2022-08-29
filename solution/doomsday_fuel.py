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
import math

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
    prob_fuel = probabilize_fuel(fuel)
    print(sum(prob_fuel[0]))

    #re_fuel = reorder_fuel(prob_fuel)
    assert False

    #uses matrix exponentiation to calculate limit as elements go to infinity
    exp_fuel = get_solution_matrix(prob_fuel)
    print(exp_fuel)
    assert False
    #print(exp_fuel)

    #formats into a single line answer
    results = format_solution(exp_fuel, fuel)
    return results



