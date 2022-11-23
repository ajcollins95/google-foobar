import sys
from solution import *

def test():
    tests = [
        ('4','7'),
        ('2','1'),
        ('2', '4')
    ]

    answers = [
        "4",
        "1",
        'impossible'
    ]

    for i in range(len(tests)):
        M = tests[i][0]
        F = tests[i][1]
        actual = solution(M, F)
        if not actual == answers[i]:
            print ("M = ", M, "F = ", F, "expected ", answers[i], ", got ", solution(M,F))

    print "Tests passed!"

test()