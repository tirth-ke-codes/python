#Program to find greatest number from given three numbers

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))

if a > b and a > c :
  print(a,"is greatest.")
elif b > c and b > a :
  print(b,"is greatest.")
elif c > a and c > b :
  print(c,"is greatest.")
