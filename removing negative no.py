#12/07/2025
#question:
# Remove Negative Numbers from a List
#code:
n = int(input("enter how many numbers to input: "))
num_list=[]
positive=[]
negative=[]
for i in range(n):
    num = int(input("enter the number: "))
    num_list.append(num)
    if num>0:
        positive.append(num)
    elif num<0:
        negative.append(num)
print("positive numbers in list:",positive)
print("negative numbers in list:",negative)
clean_list=[]
for j in num_list:
    if j>=0:
        clean_list.append(j)
print("clean list without negative number:",clean_list)
#sample:
# enter how many numbers to input: 5
# enter the number: -7
# enter the number: -8
# enter the number: -9
# enter the number: 22
# enter the number: 3
# positive numbers in list: [22, 3]
# negative numbers in list: [-7, -8, -9]
# clean list without negative number: [22, 3]
