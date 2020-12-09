#Task 4 - Yehonatan Hen , Nofar Elbaz

import math
import numpy as np

ep = 0.0001 #epsilon

def Bisection_Method(polynomial, start_point, end_point, epsilon = ep):
    """
    :param polynomial: the polynomial
    :param start_point: range start at this point
    :param end_point: range end at this point
    :param epsilon: the difference which stops the iterations of the method
    :return: root of the polynomial
    """

    iterations = -math.ceil((np.log(epsilon / (end_point - start_point))) / (np.log(2))) #np.log = ln
    i = 0
    c = (start_point + end_point) / 2
    while end_point-start_point > epsilon or c - start_point > epsilon:
        if i > iterations:
            return None
        if polynomial(start_point)*polynomial(c) < 0:
            end_point = c
        else:
            start_point = c
        c = (start_point + end_point) / 2
        i += 1

    return c


def desirableRoot(polynomial, start_point, end_point, numOfParts):
    """
    :param polynomial: the polynomial
    :param start_point: range start at this point
    :param end_point: range end at this point
    :param numOfParts: number of the parts along the range (number of "jumps" between one value to another)
    :return:the roots of the polynomial
    """

    difference = float((end_point - start_point) / numOfParts)
    roots = []

    for i in np.round(np.arange(start_point, end_point, difference), 10):
        if polynomial(i)*polynomial(i + difference) < 0:
            ans = Bisection_Method(polynomial, i, i + difference)
            if ans:
                roots.append(round(ans,5))

    dpolynomial = np.polyder(polynomial)
    for i in np.arange(start_point, end_point, difference):
        if dpolynomial(i)*dpolynomial(i+difference) < 0:
            ans = Bisection_Method(dpolynomial, i, i + difference)
            if ans and abs(polynomial(ans)) >= 0.0 and (abs(polynomial(ans))) <= ep * 0.1:
                roots.append(int(abs(ans)))

    return roots



coeff = []
i = 1
num = input("enter coefficient value " + str(i) + " ,press 's' to stop:")
while num != 's':
    coeff.append(float(num))
    i+=1
    num = input("enter coefficient value " + str(i) + " ,press 's' to stop:")

polynomial = np.poly1d(coeff)
sp = float(input("enter start point: "))
ep = float(input("enter end point: "))
parts = int(input("enter number of parts between start and end point: "))
print(desirableRoot(polynomial, sp, ep, parts))
