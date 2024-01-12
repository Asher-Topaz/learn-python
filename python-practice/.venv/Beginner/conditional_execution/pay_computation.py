inp1 = input("Enter number of hours worked: ")
inp2 = input("Enter the hourly rate: ")

try:
    hours = float(inp1)
    rate = float(inp2)
except:
    print("Error! Please enter a valid input")

if hours > 40: 
    extra_hours = hours - 40
    basic_gross_pay = (hours - extra_hours) * rate
    extra_pay = extra_hours * (rate * 1.5)
    gross_pay = basic_gross_pay+ extra_pay
else:
    gross_pay = hours * rate

print("Your gross pay is", gross_pay)


    
    
  

