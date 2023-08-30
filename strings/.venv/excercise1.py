#reverse traversal through a string

fruit = 'banana'
length = len(fruit) #get length of string fruit
index = length - 1 #index variable is 1 less than the length
#beginning of while loop
while index > -1:#condition for while loop to keep running
    letter = fruit[index]
    print(letter)
    index = index - 1

