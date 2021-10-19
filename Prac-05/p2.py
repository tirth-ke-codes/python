#Write a python program to add "ing" at the end of given string (length should be atleast 3)
#If the given string alresdy ends with "ing" then add "ly"
#If given string is less than 3 characters long, leave it unchanged

s = input("Enter a word : ") 

if len(s) >= 3:
    if s.endswith("ing"):
        res = s+"ly"
    else:
        res = s+"ing"
else:
    res = s
    
print(res)
