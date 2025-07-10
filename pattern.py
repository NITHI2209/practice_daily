#10/07/2025
#increament in numbers
total = 0
num = 1
n = int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" " , end =" ")
    for k in range(i):
        print(num,end=" ")
        total += num
        num +=1 
    print()
print("sum of pattern: ",total)
