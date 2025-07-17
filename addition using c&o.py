#17/07/2025 
#question:
# Create a class Calculator that has a method to add two numbers.
#code:
class Calculator:
    def add(self, a, b):
        return a + b

# create object
sum_num = Calculator()

# take input
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

# call the method using the object
result = sum_num.add(num1, num2)
print("Sum of numbers is:", result) 
#sample:
# Enter the number 1: 55
# Enter the number 2: 98
# Sum of numbers is: 153
