#initialized value of total and count
total=0
count=0
#start of indefinite while loop
while True:
    numbers=input('Enter a number:') #ask for user input
    #condition if user enters done 
    if numbers == 'done':
        break
    

    #try and except for when user enter non integer values
    try: 
        value = int(numbers)
    except ValueError:
        print("Not a number try again!")
        continue
    
    #calculate new values of total and count as the user enters new inputs
    total = total + value
    count = count + 1
#value for average
if count > 0:
    average = total/count
else:
    average=0

print('Count,Total,Average:',count,total,average)

    


    



    
