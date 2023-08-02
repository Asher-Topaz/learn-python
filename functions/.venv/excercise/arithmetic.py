a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
    
def add(a, b):
    x = a + b
    return x
    
def diff(a, b):
    y = a - b
    return y
    
def product(a, b):
    z = a * b
    return z
    
      
sum_number = add(a, b)
print("The sum of the two integers is",sum_number)
diff_number = diff(a, b)
print("The difference between two numbers", diff_number)
product_number = product(a, b)
print("The prodoct of two numbers is", product_number)
    
    
    
    