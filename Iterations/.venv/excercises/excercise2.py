biggest = 0
smallest = 0
while True:
    numbers=input('Enter a list of numbers:')
    if numbers == 'done':
        break


    try:
        value = int(numbers)
    except ValueError:
        print('Not a number. Please enter a number')
        continue

    if biggest == 0 or biggest < value:
        biggest = value
    if smallest == 0 or value < smallest:
        smallest = value


print("The maximumum value :",biggest)
print("The minimum value :", smallest)


   


    


        
    


