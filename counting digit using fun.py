#15/07/2025
#question:
#Function to count the number of digits in a number
#code:
def count_numbers(n):
    count = 0
    while n > 0:
        n= n//10
        count+=1 
    print("total count is:",count)

num = int(input("enter the digit: "))
count_numbers(num)
#sample:
# enter the digit: 57896739481968974
# total count is: 17
