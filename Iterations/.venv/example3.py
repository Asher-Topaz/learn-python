while True: #body of while statements keeps executing as a loop
    line = input('>') #asking user for input
    if line[0] == '#': #condition for skipping an iteration
        continue #goes back to the beginning of loop to execute next iteration
    if line == 'done': #wehen user enters done loop breaks and is exited
        break
    print(line) #prints users input on next line
print('Done!')