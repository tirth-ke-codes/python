#Find all prime nos in a given range

def isPrime(num):
  flag=True
  for i in range(2,num):
    if num % i == 0:
      flag=False
  return flag

range_s=int(input("Enter range start : "))
range_e=int(input("Enter range end : "))
prime_list=[]

for i in range(range_s,range_e+1):
  if isPrime(i) and i>1:
    prime_list.append(i)
    
print(prime_list)
 
