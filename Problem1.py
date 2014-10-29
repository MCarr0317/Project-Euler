#-------------------------------------------------------------------------------
# Name:        Problem 1
# Purpose:     Multiples of 3 and 5
#
# Author:      Matthew Carr
#
# Created:     01/07/2014

#-------------------------------------------------------------------------------
"""This code creates a list of numbers from 1 to 999 and finds the Sum of
all numbers that are multiples of 3 or 5
"""
def main():
    def find_multiples():
        List = []
        for i in range(1, 1000):
            if i % 3 == 0 or i % 5 == 0:
                List.append(i)

        Sum = 0
        for i in range(len(List)):
            Sum += List[i]

        print "sum is ", Sum


    List = find_multiples()


if __name__ == '__main__':
    main()
