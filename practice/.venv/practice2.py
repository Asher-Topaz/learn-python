hours = input('Enter hours worked\n')
rate = input('Enter rate worked \n')

hrs = float(hours)
r = float(rate)

if hrs > 40:
    ogp = hrs * r
    egp = (hrs - 40) * (r * 0.5)
    gp = (ogp + egp)
    print("Your new pay is: ")


else: 
    gp = (hrs * r)
print("Your pay is:  ", gp)
