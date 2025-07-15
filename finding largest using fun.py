#15/07/2025
#question:
# Write a function that accepts three numbers and prints the largest among them.
#code:
def largest(a,b,c):
    if a>b and a>c:
        print(f"{a} is largest")
    elif b>a and b>c:
        print(f"{b} is largest")
    else:
        print(f"{c} is largest")
num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))
num3 = int(input("enter the number 3: "))
largest(num1,num2,num3)
#sample:
# enter the number 1: 67
# enter the number 2: 98
# enter the number 3: 105
# 105 is largest
