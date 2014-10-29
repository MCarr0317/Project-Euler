#-------------------------------------------------------------------------------
# Name:        Project Euler problem 9
# Purpose:
#
# Author:      Matt
#
# Created:     08/01/2014
# Copyright:   (c) Matt 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time

#pythagorean triplet
def find_triplets(n):
    a = range(n)
    b = range(n)
    c = range(n)

    for i in xrange(n):
        for x in xrange(n):
            for y in xrange(n):
                if a[x]*a[x] + b[y]*b[y] == c[i]*c[i] and (a[x] != 0 and b[y] != 0 and c[i] != 0):
                    #print a[x], " ", b[y], " ", c[i]
                    if a[x]+b[y]+c[i] == 1000:
                        print "a: ", a[x], " b: ", b[y], " c: ", c[i], " product: ", a[x]*b[y]*c[i]
                        return True


    return False


start = time.clock()
n = 500 #arbitrary base range

while not find_triplets(n):
    n += 100
    find_triplets(n)


finish = time.clock()
print "Time Taken: ", (finish-start) , " seconds"
