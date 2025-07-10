#10/07/2025
#finding index of search num
n = int(input("enter the num a list should have: "))
num=[]
for i in range(n):
    x=int(input("enter the numbers inside the list: "))
    num.append(x)
print(num)
search_num = int(input("enter the number: "))
index=num.index(search_num)
if search_num in num:
    print(f"{search_num} is prsent in num")
else:
    print(f"{search_num} is not in num")
print("Index of search number is: ",index)
