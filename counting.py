# counting even and odd count in a list
#10/07/2025
n = int(input("enter the num a list should have: "))
num=[]
even=0
odd=0
for i in range(n):
    x=int(input("enter the numbers inside the list: "))
    num.append(x)
print(num)
for x in num:
    if x %2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print("odd:",odd)
