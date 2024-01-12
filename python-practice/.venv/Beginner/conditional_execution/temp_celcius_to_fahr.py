inp = input("Enter fahrenheit temparature: ")

try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5/9
    print(cel)
except:
    print("please enter a number")

