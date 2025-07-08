#08/07/2025 
n = int(input("enter the number: "))
flag = 0
if n <= 1:
    print("its not a prime number")
else:
    for i in range(2,n):
        if n%i == 0:
            flag = 1 
            break
if flag == 1:
    print(f"{n} is not a prime")
else:
    print(f"{n} is a prime nos")
