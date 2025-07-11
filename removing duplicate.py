#11/07/2025
#Question:
#Given a list of integers, write a Python program to remove all duplicate elements while preserving the order of the first occurrence.
#code:
a = int(input("enter how many numbers to be in list: "))  # Step 1: Get number of inputs
b = []  # Original list
c = []  # List without duplicates

# Step 2: Take inputs from user
for i in range(a):
    num = int(input("enter the numbers to be in list: "))
    b.append(num)

print(b)  # Step 3: Print original list

# Step 4: Remove duplicates while keeping order
for j in b:
    if j in c:
        continue  # Skip if already added
    else:
        c.append(j)

print(c)  # Step 5: Print result without duplicates
#sample:
# enter the how many numbers to be in list: 5
# enter the numbers to be in list: 1
# enter the numbers to be in list: 2
# enter the numbers to be in list: 2
# enter the numbers to be in list: 3
# enter the numbers to be in list: 4
# [1, 2, 2, 3, 4]
# [1, 2, 3, 4]
