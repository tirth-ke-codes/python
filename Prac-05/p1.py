# Program to demonstrate various operations of string in python 

s1="python in VSCode"
s2="ALL UPPERCASE"
s3="all lowercase"
s4="python:in:VSCode"

a = s1.find('C')
print(a,"\n")

b1 = s1.isupper()
print(b1)
b2 = s2.isupper()
print(b2)
b3 = s3.islower()
print(b3,"\n")

c=s1.replace("VSCode","Pycharm")
print(c,"\n")

d1=s1.split()
print(d1)
d2=s4.split(":")
print(d2,"\n")

e=s1.title()
print(e)
f=s1.capitalize()
print(f)
g=s1.casefold()
print(g,"\n")

h=s1.count("o")
print(h,"\n")
