nums = [1,1,1,3,3,4,3,2,4,2]
def duplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
print(duplicate(nums))
