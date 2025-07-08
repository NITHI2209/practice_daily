# 08/07/2025
word = input("enter the character: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
count = 0
#both upper and lower is included
for i in word:
    if i in vowels:
        count+=1 
print(f"{count} = count of vowels")
