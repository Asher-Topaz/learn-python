import random
names_string = input("Give me everyones neame separated bv comma ")


names = names_string.split(",")

print(names)
num_items = len(names)
random_choice = random.randint(0,num_items-1)

print(f"The person to pay is {names[random_choice]}")

