age = (input("What is your current age ? "))
max_age = 90

try:
    years_lived = int(age)
except:
    print("Error ! Please enter an integer value.")

years_left = max_age - years_lived

months_left = years_left * 12

weeks_left = round(years_left * 52.1)

days_left = years_left * 365

print(f"You have {days_left} days,{weeks_left} weeks, {months_left} months and {years_left} years left")





