#finding the largest value in a list or sequence

largest = None #initial value of varible largest
print('Before:',largest) #print initial value of largest

for itervar in [3,41,12,9,74,15]: #start of for loop
    if largest is None or itervar > largest: #condition for value of largest
        largest = itervar
    print('Loop',itervar,largest) #print current value of largest and itervar in the iteration of the loop
print('Largest',largest) #the final iteral value of largest

