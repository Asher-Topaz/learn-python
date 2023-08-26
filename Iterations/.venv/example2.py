while True:#loop is always true
    line = input('>') #asking user for input as long as done is not inputed
    if line == 'done': #when user enters done loop breaks and is excited
        break
    print(line) #keeps printing until break is activated by user entering done
print('Done!')