def computegrade(score):
    if score >= 0.9:
        return 'A'
        
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'c'
    elif score >= 0.6:
        return 'D'
    elif score < 0.6:
        return 'F'

x=computegrade(0.95)
print(x)


