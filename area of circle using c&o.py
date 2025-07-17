#17/07/2025
#question:
#Create a class Circle with a method to calculate the area of a circle.
#code:
class area:
    def circle_area(self,radius):
        return 3.14*radius*radius
        
area_of_circle = area()

radius = int(input("enter the radius of circle: "))

result = area_of_circle.circle_area(radius)
print("Area of circle:",result) 
#sample:
# enter the radius of circle: 5
# Area of circle: 78.5
