print("Welcome to the tip calculator")
total_bill = float(input("What is the toal bill  $ "))

tip = int(input("What amount of tip would you like to give ? 10, 12 or 15 "))

people = int(input("How many people to split the bill ? "))

tip_in_percentage = tip/100

tip_amount = (tip_in_percentage * total_bill)

bill = tip_amount + total_bill

bill_per_person = (bill / people)

final_bill = round(bill_per_person,2)

print(f"Your final bill is  $ {final_bill} per person")





