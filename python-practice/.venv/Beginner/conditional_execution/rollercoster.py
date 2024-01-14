print("Welcome to the rollercoster! ")
height = int(input("What is your height in Cm? "))
bill = 0
if height > 120:
    print("You can rid the rollercoster")
    age = int(input("What is your age? "))
    if age >= 18:
        bill = 12
        print("Your riding fee is $12 ")
    elif age < 12:
        bill = 5
        print("Your riding fee is $5")
        
    elif age  >= 45 and age <= 55:
        print("have a free ride on us")

    else:
        bill = 7
        print("Your riding fee is 7$")

    wants_photo = input("Do you want to take a photo. Y or N")
    if wants_photo == 'Y':
        bill = bill + 3
    print(f"Your final bill is {bill}")


else:
    print("Sorry you are too short to ride")

