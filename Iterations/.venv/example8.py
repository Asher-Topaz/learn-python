smallest = None #initial value of variable smallest
print('Before:',smallest) #print initial value of smallest
#beginning of for loop
for itervar in [3,41,12,9,74,15]: #iteration variable and list of numbers
    if smallest is None or itervar < smallest: #condition for value of smallest
        smallest = itervar
    print('Loop:',itervar, smallest) #print iteral values of smallest values of itervar
print('Smallest:',smallest)


