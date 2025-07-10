#10/07/2025
#average of nos from list
n = int(input("enter the num a list should have: "))
num=[]
average=0
total = 0
for i in range(n):
    x=int(input("enter the numbers inside the list: "))
    num.append(x)
print(num)
for j in (num):
    total+=j
average = total/n
print("average is:",average)
