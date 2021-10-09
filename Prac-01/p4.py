#perform basic oprerations in python
n1=int(input("Enter Number 1 : "))
op=str(input("Enter Operator : "))
n2=int(input("Enter Number 2 : "))
if op == '+':
  print("Sum is :", n1+n2)
elif op == '-':
  print("Difference is :", n1-n2)
elif op == '*':
  print("Product is :", n1*n2)
elif op == '/':
  print("Answer is :", n1/n2)
else:
  print("Invalid operator") 
