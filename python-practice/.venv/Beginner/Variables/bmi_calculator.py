height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg"))

bmi = weight/(height**2)

integer_bmi = int(bmi)

print(integer_bmi)