#10/07/2025
even = 0
odd = 0
n = int(input("enter the number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        even += i  # adds even numbers
    else:
        odd += i   # adds odd numbers

print("Even:", even)
print("Odd:", odd)
