#17/07/2025
#question:
#Create a class Square with a method to calculate the square of a number.\
#code:
class Calculator:
    def square(self, a):
        return a * a

sum_num = Calculator()

num1 = int(input("Enter the number: "))

result = sum_num.square(num1)
print("Square of the number:", result)
#sample:
# Enter the number: 5
# Square of the number: 25
