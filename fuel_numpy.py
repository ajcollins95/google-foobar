from fractions import Fraction
import numpy as np
from numpy.linalg import matrix_power
import matplotlib.pyplot as plt
#
#
#MAKE THIS BEAUTIFUL
#THIS IS NOT MINE!!! USed fot testing
#
#
def solution(m):
    if len(m) < 2:
        return [1,1]
    r_subm, q_subm = split_martix(m)
    f_subm = calc_f(q_subm)
    print(r_subm)
    print(f_subm)
    fr_subm = np.dot(f_subm, r_subm)
    return fr_subm
    #return dec_to_frac_with_lcm(fr_subm[0])

def split_martix(m):
    absorbing = set()
    for row_i in range(len(m)):
        if sum(m[row_i]) == 0:
            absorbing.add(row_i)
    r_subm = []
    q_subm = []
    for row_i in range(len(m)):
        if row_i not in absorbing:
            row_total = float(sum(m[row_i]))
            r_temp = []
            q_temp = []
            for col_i in range(len(m[row_i])):
                if col_i in absorbing:
                    r_temp.append(m[row_i][col_i]/row_total)
                else:
                    q_temp.append(m[row_i][col_i]/row_total)
            r_subm.append(r_temp)
            q_subm.append(q_temp)
    return r_subm, q_subm

def calc_f(q_subm):
    return np.linalg.inv(np.subtract(np.identity(len(q_subm)), q_subm))

def dec_to_frac_with_lcm(l):
    ret_arr = []
    denoms = []
    for num in l:
        frac = Fraction(num).limit_denominator()
        ret_arr.append(frac.numerator)
        denoms.append(frac.denominator)
    lcd = 1
    for denom in denoms:
        pass
        #lcd = lcm(lcd,denom)
    for num_i in range(len(ret_arr)):
        ret_arr[num_i] *= int(lcd/denoms[num_i])
    ret_arr.append(lcd)
    return ret_arr

test = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

test2 =[
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],

        ]

gamble = [
    [0,0,0,0,0,0],
    [3,0,2,0,0,0],
    [0,3,0,2,0,0],
    [0,0,3,0,2,0],
    [0,0,0,3,0,2],
    [0,0,0,0,0,0]
]

#solution(test)



def solver(fuel):
    std_fuel = np.array(standardizeFuel(fuel))
    absorbed = absorbStates(std_fuel)
    fractional_array = fractionalize(absorbed)
    print (fractional_array)
    #print(Fraction(absorbed[1][0]).limit_denominator(2147483647))
    

def areInnerStatesZero(fuel, epsilon):
    
    for i in range(len(fuel)):
        short_row_i = fuel[i][1:len(fuel) - 2]
        short_row_sum = np.sum(short_row_i)
        #print(short_row_sum > epsilon)
        #print(f'SRS: {short_row_sum}, SRS > Epsilon: {short_row_sum > epsilon}')
        if short_row_sum > epsilon:
            return False
    return True
        

    
def absorbStates(std_fuel):
    epsilon = float(10) ** -12
    power = 20
    are_inner_states_zero = False
    x = []
    y = []
    (row,col) = (1,0)
    #while(not are_inner_states_zero):
    while(power < 30):
        exp = matrix_power(std_fuel, power)
        print(14 * exp)
        are_inner_states_zero = areInnerStatesZero(exp, epsilon)
        #print(f'Power: {power}')
        value = exp[row][col].copy()
        print(value)
        x.append(power)
        y.append(exp[row][col].copy())
        power += 1
    plot(x,y)
    return exp

def standardizeFuel(fuel):
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

def fractionalize(absorbed):
    max_32_bit = 2147483647
    result = []
    
    for i in range(len(absorbed)):
        row_i = absorbed[i]
        temp_row =[]
        for k in [0, len(absorbed) - 1]:
            fractional_elem = Fraction(row_i[k]).limit_denominator(max_32_bit)
            temp_row.append(fractional_elem)
        result.append(temp_row)
    return result

def plot(x,y, x_label = "", y_label = ""):
    assert len(x) == len(y)
    fig = plt.figure()
    print(x,y)
    print("plotting")
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


solver(test)
