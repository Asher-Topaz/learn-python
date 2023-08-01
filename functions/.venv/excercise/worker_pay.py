def computepay(hrs, r):
    h = float(hrs)
    rh = float(r)
    if h <= 40:
        gp = rh*h
    elif h > 40:
        ogp = rh * h
        egp = (h-40) * (rh * 0.5)
        gp = ogp + egp
    return gp

x = computepay(45, 10)
print(x)





    

    