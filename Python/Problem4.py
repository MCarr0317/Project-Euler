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
"""finds the largest palindrome made from the product of two 3 digit numbers"""

def main():
    def palindrome(number):
        copy = str(number)

        if copy == copy[::-1]:
            return True
        else:
            return False


    three_digit_nums = []
    for i in range(100, 1000):
        three_digit_nums.append(i)


    products = []
    for i in range(0, len(three_digit_nums)):
        for y in range(0, len(three_digit_nums)):
            products.append(three_digit_nums[i] * three_digit_nums[y])


    palindromes = []
    largest = None
    for i in range(len(products)):
        if palindrome(products[i]) and products[i] > largest:
            palindromes.append(products[i])
            largest = products[i]


    print largest

if __name__ == '__main__':
    main()
