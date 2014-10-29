#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matt
#
# Created:     07/01/2014
# Copyright:   (c) Matt 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""Finds the largest prime factor of a given number using fermats factorization
"""
import math

def main():
    def prime_factors(n):
        factors = []
        d = 2
        while n > 1: #until we have checked all numbers above 1
            while n % d == 0: #while the number is divisible by d
                factors.append(d)   #that means it is a factor
                n /= d #divide n by its divisor
            d = d + 1

        largest = None
        for i in range(len(factors)):
            if factors[i] > largest:
                largest = factors[i]


        print largest



    prime_factors(600851475143)


if __name__ == '__main__':
    main()
