num1 = float(input("Enter a number1:"))
num2 = float(input("Enter a number2:"))
ope = input("Enter a operator(+,-,*,/):")
if ope == "+":
    result = num1 + num2
elif ope == "-":
    result = num1 - num2
elif ope == "*":
    result = num1 * num2
elif ope == "/":
    if num2 != 0:
       result = num1 / num2
    else:
       result = ("Error! Division by zero")
else:
    result = ("Invalid Operator")
    
print("Result:",result)