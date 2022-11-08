import math

CACHE = []
def main(n):
    CACHE = [['-' for c in range(n+1)] for r in range(n+1)]
    maxS = math.floor(((8 * n  + 1) ** 0.5 - 1) / 2)
    for k in range(int(maxS)):
        Q(n, k)
    print CACHE
    #return Q(n ,maxS)
"""
def Q(n, k):
    if n == k == 1:
        return 1
    elif n > 0 and k == 0:
        return 0
    elif n < k or k < 1:
        return 0
    else:
        return Q(n - k, k) + Q(n - k, k-1)
"""
