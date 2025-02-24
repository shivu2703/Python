number1 = 10
number2 = 5

def addition(num1, num2):
    add = num1 + num2
    return add
    

def substraction(num1, num2):
    sub = num1 - num2
    return sub
    

def multiply(num1, num2):
    multi = num1 * num2
    return multi
    

def division(num1, num2):
    div = num1 / num2
    return div

# Call the addition function
print("addition of the number:-"+ str(addition(number1,number2)))

# Call the substraction function 
print("substraction of the number:-"+ str(substraction(number1, number2)))

# Call the multiply function
print("multiply of the number:-"+ str(multiply(number1, number2)))

# Call the division function 
print("division of the number:-"+ str(division(number1, number2)))
