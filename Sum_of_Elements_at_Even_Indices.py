#04/08/2025
#question
#Write a Python program to calculate the sum of elements at even indices in a list.
#code:
Input = [10, 20, 30, 40, 50]  
count = 0
for i in range(len(Input)):
    if i % 2 == 0:
        count += Input[i]
print(count)
        
