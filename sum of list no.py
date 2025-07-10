#10/07/2025
n = int(input("enter the num a list should have: "))
num=[]
total=0
for i in range(n):
    x=int(input("enter the numbers inside the list: "))
    num.append(x)
print(num)
for j in (num):
        total+=j
print("Total is:",total)
