def is_leap(year): #function declaration
    leap = False #default value of user input
    
#conditions required for user input to be a leap year
    if (year % 4) ==0: 
        leap=True
    if(year % 100) == 0:
        leap = False
        if (year % 400) == 0:
            leap = True

    # return the boolean result of true or false
    return leap


year=int(input("Enter any year to see if its a leap year\n"))
print((is_leap(year)))






