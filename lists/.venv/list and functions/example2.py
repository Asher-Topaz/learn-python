#create an empty list
numlist = list()

#create while loop to iterate through list
while (True):
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    value = float(inp)

    numlist.append(value)

#use in built function sum and length
average = sum(numlist)/len(numlist)
print('Average:',average)

