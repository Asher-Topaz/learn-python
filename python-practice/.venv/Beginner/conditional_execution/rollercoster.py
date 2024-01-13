print("Welcome to the rollercoster! ")
height = int(input("What is your height in Cm? "))

if height > 120:
    print("You can rid the rollercoster")
    age = int(input("What is your age? "))
    if age >= 18:
        print("Your riding fee is $12 ")
    elif age < 12:
        print("Your riding fee is $5")

    else:
        print("Your riding fee is 5$")

else:
    print("Sorry you are too short to ride")

