#function definition
def min(values): #function parameter
    smallest = None #initialized variable befor loop start
    #start of the for loop 
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest #return value

numbers = [5,8,20,10,2,16,100]

print("Smallest :",min(numbers))
