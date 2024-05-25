def computepay(hrs, r):
    if hrs > 40:
        extr_hrs = hrs - 40
        gross_pay = (hrs - extr_hrs) * r
        extr_pay = (extr_hrs * (r * 1.5))
        actual_gross_pay = gross_pay + extr_pay
    else:
        actual_gross_pay = hrs * r
    
    return actual_gross_pay


 

inp1 = float(input('Enter number of hours worked'))
inp2 = float(input('Enter hourly rate'))

pay = computepay(inp1,inp2)
print(pay)

    