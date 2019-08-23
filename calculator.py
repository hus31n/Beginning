def calculate():
    num1 = input("firstnum")
    while check(num1) == False:
        num1 = input("firstnum")
    else :
        num1 = float(num1)
    
    op = input("operator")
    while opcheck(op) == False:
        op = input("operator")
    
    num2 = input("secnumber")
    while check(num2) == False:
        num2 = input("secnumber")
    else :
        num2 = float(num2)

    if op == "+":
        plus(num1,num2)
    elif op == "-":
        subtract(num1,num2)
    elif op == "/":
        division(num1,num2)
    elif op == "*":
        multiply(num1,num2)

def plus(a,b):
    print(a + b)
    
def subtract(a,b):
    print(a - b)
    
def division(a,b):
    print (a / b)
    
def multiply(a,b):
    print (a * b)
def opcheck(a):
    if a == "+":
        return True
    elif a == "-":
        return True
    elif a == "/":
        return True
    elif a == "*":
        return True
    else :
        return False

def check(s):
    try:
        float(s)
        return True
    except:
        return False
        
calculate()

