#-------------------------------------------------------------------------------
# Name:        Project Euler problem 10
# Purpose:
#
# Author:      Matt
#
# Created:     08/01/2014
# Copyright:   (c) Matt 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#http://en.wikipedia.org/wiki/Primality_test


import time



#function to test if a number is prime
def isPrime(num):
    if num <= 1:    #if num is 1, return false (not prime)
        return False
    elif num == 2:  #if num is 2, return true (first prime number)
        return True
    elif num % 2 == 0: #if num is even, return false (all primes other than 2 are odd)
        return False

    count = 3           #since we have 1 and 2 covered, we start at the number 3

    while count*count <= num:   #until count is the sqrt of num (becomes redundant after this)
        if num % count == 0:    #if count divides num, our number
            return False        #   has a divisor other than 1 and itself, so return false
        else:
            count += 2          #else, try the next odd number

    return True                 #if we get to sqrt of num and there were no divisors,
                                #   then num is clearly prime

start = time.clock()

num = 1
Sum = 2

while num < 6:
    if isPrime(num):
        Sum += num

    num += 2







print "sum is ", Sum
finish = time.clock()
print "Time Taken: ",(finish-start), " seconds"
