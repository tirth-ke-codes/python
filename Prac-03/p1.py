# Program to tale matks of 5 subjects out of 100 and print grade

marks=[]
for i in range(0,5):
    marks.append(int(input("Enter marks of subject " + str(i+1) + " out of 100 : ")))
p=(sum(marks)/500)*100

print("Percentage = ",p)
