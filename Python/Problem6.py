#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matt
#
# Created:     08/01/2014
# Copyright:   (c) Matt 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

def sum_of_squares(numbers):
    Sum = 0
    for i in range(len(numbers)):
        Sum += numbers[i]*numbers[i]

    return Sum


def square_of_sums(numbers):
    Sum = 0
    for i in range(len(numbers)):
        Sum += numbers[i]

    return Sum*Sum


start = time.clock()
range_numbers = 100
numbers = range(1, range_numbers+1)

print "difference is ", abs(sum_of_squares(numbers)-square_of_sums(numbers))
finish = time.clock()
print "time taken: ",float(finish-start)*1000, " ms"
