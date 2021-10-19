# To make a simple calculator

a=float(input("Enter number 1 : "))
op=input("Enter operator : ")
b=float(input("Enter number 2 : "))

if op == '+':
    print("Sum is",a+b)
elif op == '-':
    print("Difference is",a-b)
elif op == '*':
    print("Product is",a*b)
elif op == '/':
    print("Division is",a/b)
else:
    print("Invalid operator.")
