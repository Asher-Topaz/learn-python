
#create empty list
catNames = []

#create while loop for user to enter input of list items
while True:
    print("Enter the name of cat" + str(len(catNames) + 1 ) +
        '(Or enter nothing to stop.):')
    
    name = input()
    if name == '':
        break
    #concatenate input to list
    catNames = catNames + [name]

print("The cat names are: ")
#for loop to iterate through list

for name in catNames:
    print(' ' + name)
