user_input = input("Enter farenheint temperature:   ")
try:
    farnh = float(user_input)
    cel = (farnh - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print("Wrong! Enter correct format")
