#-------------------------------------------------------------------------------
# Name:        Problem 2
# Purpose:
#
# Author:      Matthew Carr
#
# Created:     01/07/2014
#-------------------------------------------------------------------------------
"""
    This program computes the fibonnaci series only while the current value
    is less than 4 million, then finds the sum of the even numbers
"""
def main():
    def fibonnaci():
        Fib = [1, 2]
        position = 0
        new_val = 0
        while new_val <= 4000000:
            new_val = Fib[position] + Fib[position+1]
            if new_val <= 4000000:
                Fib.append(new_val)
                position += 1

        Sum = 0
        for i in range(len(Fib)):
            if Fib[i] % 2 == 0:
                Sum += Fib[i]

        print Sum


    fibonnaci()

if __name__ == '__main__':
    main()
