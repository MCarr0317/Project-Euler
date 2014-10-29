#-------------------------------------------------------------------------------
# Name:        Project 12
# Purpose:
#
# Author:      Matt
#
# Created:     01/02/2014
# Copyright:   (c) Matt 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math, time

#generates the entire sequence in a list
def generate_sequence(limit = 1):
    sequence = []
    n = 1

    while (n <= limit):
        sum = 0
        for i in xrange(1, n+1):
            sum += i

        n += 1
        sequence.append(sum)


    return sequence


#generates the next term in the sequence
def generate_next_term(length):
    num = length+1
    sum = 0
    for i in xrange(1, num+1):
        sum += i

    return sum


#returns the number of factors of a number
def num_of_factors(num):
    num_factors = 0
    for i in xrange(1, int(math.sqrt(num))+1):
        if num % i == 0:
            num_factors += 2

    if int(math.sqrt(num)) * int(math.sqrt(num)) == num:
        num -= 1

    return num_factors


#returns a list containing all the factors for all the numbers in the sequence
def factor_sequence(sequence):
    sequence_factors = []


    for i in xrange(len(sequence)):
        sequence_factors.append(factor_number(sequence[i]))



    return sequence_factors




def main():
    start = time.clock()
    n = 0
    num = num_of_factors(generate_next_term(n))



    while num <= 500:
        n += 1
        num =num_of_factors(generate_next_term(n))

    finish = time.clock()


    print generate_next_term(n), " has ", num, " factors"
    print "took: ", (finish-start), " seconds"

if __name__ == '__main__':
    main()
