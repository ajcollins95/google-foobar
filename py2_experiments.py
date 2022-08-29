from fractions import Fraction, gcd

def lcm(numbers):
    lcm = 0
    num_last = numbers[0]
    for i in range(len(numbers)):
        num_i = numbers[i]
        lcm_i = abs(num_i * num_last) // gcd(num_i, num_last)
        if lcm_i > lcm:
            lcm = lcm_i
    return lcm

#print(lcm([3,7,21]))