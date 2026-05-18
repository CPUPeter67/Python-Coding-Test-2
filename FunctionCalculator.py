print("In this program, your input will be used to calculate the result of basic arithmetic operations.")
def addition(a, b):
    return(a + b)
def subtraction(a, b):
    return(a - b)
def multiplication(a, b):
    return(a * b)
def division(a, b):
    return(a / b)

number1 = float(input("Enter the value for the first number: "))
number2 = float(input("Enter the value for the second number: "))

print("The addition function's result is: ", addition(number1, number2))
print("The subtraction function's result is: ", subtraction(number1, number2))
print("The multiplication function's result is: ", multiplication(number1, number2))
print("The division function's result is: ", division(number1, number2))

try:
    division(number1, number2)
except ZeroDivisionError:
    print("You cannot divide by zero. You will always achieve zero!")
except ValueError:
    print("Your input is not numerical! Please enter the correct value.")