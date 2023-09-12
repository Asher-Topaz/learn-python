#creating empty list
carBrands = []

#creating while loop
#to iterate through user input
#store user input in list

while True: 
    print("Enter name of car brand " + str(len(carBrands)+1 ) + 
        " and enter nothing when your done")
    
    car = input()
    if car == '':
        break

    #put user input into list
    carBrands = carBrands + [car]

print("The car brand names are: ")
for car in carBrands:
    print(" " + car)
    

