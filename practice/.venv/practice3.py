hours = input('Enter number of hours worked:  ')
rate = input("Enter rate per hour:   ")

try:
    hrs = float(hours)
    r = float(rate)
    quit()

except:
    print('Enter correct input  ')

if hrs > 40:
    ogp = hrs * r
    ngp = (hrs - 40) * (0.5 * r)
    gp = (ogp + ngp)
    print('Your pay is:   ',gp)

elif hrs < 40:
    gp = hrs * r 
    print("Your pay is: ",gp)



