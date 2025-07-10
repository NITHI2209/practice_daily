#10/07/2025
num = [10, 90, 88, 87, 96, 54]
smallest = num[0]  # Start by assuming the first number is the largest

for i in num:
    if i < smallest:
        smallest = i

print("smallest number is:", smallest)
