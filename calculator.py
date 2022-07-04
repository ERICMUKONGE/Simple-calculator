num1 = float(input("Enter first number of your choice:\n"))
operator = input("Enter any operator of your choice:\n")
num2 = float(input("Enter second number of your choice:\n"))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
else:
    print("Invaid operator chosen")                