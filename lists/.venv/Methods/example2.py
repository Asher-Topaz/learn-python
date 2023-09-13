#create empty list

span = []

#create while loop

while True:
    #ask user for input
    word = input('Enter strings and enter done when finished \n')
    #condition to break when user enters 'done'
    if word == 'done':
        break

    #pass user input into empty list with append() function
    span.append(word)

print("\n The list you entered is: \n ", span)

index =int(input("Enter the index of item in list to display \n:  "))

#condition to print out index item 
#after user input

if index in range(len(span)-1):
    print("The item of index  " + str(index) + " is :" + span[index])





