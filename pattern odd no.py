# 10/07/2025
# increamenting numbers in right angle triangle (odd numbers)
total = 0
num = 1 
n =  int(input("enter the number of rows: "))
for i in range(1,n):
    for j in range (i):
        print(num , end=" ")
        total += num
        num +=2
    print()
print("sum of the pattern is : " , total)
