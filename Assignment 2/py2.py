#functions to calculate 
def add(a,b):
    return a + b
def mult(a,b):
    return a * b 
def div(a,b):
    if b == 0:return "Can't divide by Zero"
    return a / b 
def flodiv(a,b):
    if b == 0:return "Can't divide by Zero"
    return a // b 
def exp(a,b):
    return a ** b 

#input 
num = int(input("Enter a number :"))
num1 = int(input("Enter a number :"))

#print 
print(f"Sum is {add(num,num1)}")
print(f"Product  is {mult(num,num1)}")
print(f"Division is {div(num,num1)}")
print(f"Floor Division is {flodiv(num,num1)}")
print(f"Exponentiation  is {exp(num,num1)}")