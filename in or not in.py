#11/07/2025
# searching a number in list
n = int(input("enter the num a list should have: "))
num=[]
for i in range(n):
    x=int(input("enter the numbers inside the list: "))
    num.append(x)
print(num)
search_num = int(input("enter the number: "))
if search_num in num:
    print(f"{search_num} is prsent in num")
else:
    print(f"{search_num} is not in num")
