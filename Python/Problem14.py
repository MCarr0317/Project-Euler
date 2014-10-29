#-------------------------------------------------------------------------------
# Name:        project 14
# Purpose:
#
# Author:      Matt
#
# Created:     01/02/2014
# Copyright:   (c) Matt 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def change_number(number):
    if number % 2 == 0:
        return float(number/2)
    elif number % 2 != 0:
        return (3*number)+1

def length_of_chain(start_num):
    num = start_num
    length = 0

    while num != 1:
        #print num
        length += 1
        num = change_number(num)

    length += 1
    return length



def main():
    biggest_startnum = 1

    for i in xrange(500001, 1000001):
        if length_of_chain(i) > length_of_chain(biggest_startnum):
            biggest_startnum = i
           # print length_of_chain(biggest_startnum)


    print biggest_startnum


if __name__ == '__main__':
    main()
