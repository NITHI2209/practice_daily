#17/07/2025
#question:
#Finding area of rectangle using class & object
#code:
class Area:
    def rectangle_area(self, a, b):
        return a * b

rc = Area()
l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of rectangle: "))

result = rc.rectangle_area(l, b)
print("Area of rectangle:", result)
#sample:
# Enter the length of rectangle: 8
# Enter the breadth of rectangle: 5
# Area of rectangle: 40
