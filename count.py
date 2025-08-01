#01/08/2025
#question:
# Problem Statement:
# Given a list of integers, count how many elements are greater than the element immediately before them.
#code:
nums = [1, 3, 2, 4, 5]
# Output: 3
left = 0 
count = 0
for right in range(1,len(nums)):
    if nums[left] < nums[right]:
        count += 1
    left += 1 
print(count)
