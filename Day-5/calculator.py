import sys

def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    multi = num1 * num2
    return multi

def div(num1, num2):
    div = num1 / num2
    return div

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "add":
    output= add(num1, num2)
    print("addition of the number: "+ str(output))

elif operator == "sub":
    output= sub(num1, num2)
    print("substraction of the number: "+ str(output))

elif operator == "mul":
    output= mul(num1, num2)
    print("multiply of the number: "+ str(output))

else:
    output = div(num1, num2)
    print("division of the number: "+ str(output))
