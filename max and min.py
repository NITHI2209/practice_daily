#12/07/2025
#question:
# Find the maximum and minimum numbers manually (using basic comparisons only, not max()/min()).
#code:
a = int(input("Enter how many numbers to input: "))
num_list = []

for i in range(a):
    num = int(input("Enter a number: "))
    num_list.append(num)

# Assume first number is both max and min
maximum = num_list[0]
minimum = num_list[0]

for number in num_list:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

print("List of numbers:", num_list)
print("Maximum number is:", maximum)
print("Minimum number is:", minimum)
# sample:
# Enter how many numbers to input: 4
# Enter a number: 33
# Enter a number: 56
# Enter a number: 78
# Enter a number: 99
# List of numbers: [33, 56, 78, 99]
# Maximum number is: 99
# Minimum number is: 33
