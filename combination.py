#14/08/2025
#find the possible combination
nums = [1, 2, 3]
k = 2  # how many elements to choose
combinations_list = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):  # ensure no repetition
        combinations_list.append([nums[i], nums[j]])
print(combinations_list)
