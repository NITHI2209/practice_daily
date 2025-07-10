#10/07/2025
# reversing odd number right angle triangle
total = 0
n = int(input("Enter the number of rows: "))

# Step 1: Calculate total number of elements in the triangle
count = n * (n + 1) // 2

# Step 2: Find the largest odd number to start with
num = 1 + (count - 1) * 2  # last odd number in the pattern

# Step 3: Print the pattern
for i in range(n, 0, -1):
    for j in range(i):
        print(num, end=" ")
        total += num
        num -= 2  # move to previous odd number
    print()

print("Sum of the pattern is:", total)
