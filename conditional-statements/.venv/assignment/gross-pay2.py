hrs = input('Enter number of hours:')
rph = input('Enter rate per hour:')
try:
    h=float(hrs)
    rh=float(rph)
except: 
    print('Error, please enter numeric input')
    quit()

if h <= 40:
    gp=rh*h
    print('Gross pay is:',gp)

elif h > 40:
    ogp=rh*h
    egp=(h-40) * (rh*0.5)
    gp = ogp + egp
    print('Gross pay is:',gp)
print('Done')









