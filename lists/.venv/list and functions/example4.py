numbers = []

while True:
    inp = input('Enter a number ')
    
    if inp == 'done':
        break
    value = float(inp)

    numbers.append(value)

for index, item in enumerate(numbers):
    print("The index " + str(index) + "  value in item is ", item)




  

