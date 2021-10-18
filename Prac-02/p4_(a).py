#Find all prime nos in a given range --without using a function--

r_start=int(input("Start : "))
r_end=int(input("Start : "))

for num in range(r_start,r_end):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
