#question
#find the all possible permutation for the given nums
nums = [1, 2, 3]
k = 2  # how many elements to arrange
permutations_list = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:  # don't use the same element twice
            permutations_list.append([nums[i], nums[j]])
print(permutations_list)
