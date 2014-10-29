#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Matt
#
# Created:     07/01/2014
# Copyright:   (c) Matt 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



num = 20
done = False

count = 0
List = []



for i in range(1, 21):
    List.append(i)


while done == False:
    #print num
    for i in range(len(List)):
        if num % List[i] == 0: # if divides evenly, increment the count
            count += 1
        elif num % List[i] != 0:# if doesnt divide evenly, reset count , change the number and start over in a new list
            count = 0
            num += 20
            break
        if count == 20:
            done = True
            print num
  
  
