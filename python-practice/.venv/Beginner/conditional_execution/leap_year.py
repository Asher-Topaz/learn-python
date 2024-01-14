year = int(input("Enter any year to check if its a leap year "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Yes! The year {year} is a leap year ")
        else:
            print(f"No! The year {year} is not a leap year")
    else:
        print(f"The year {year} is a leap year")       
else:
    print(f"No! The year {year} is not a leap year")
  

    
    

