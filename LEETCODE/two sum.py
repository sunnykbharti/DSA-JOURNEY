def twoSum(nums,target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            print(numMap)
            return [numMap[complement], i]
        numMap[nums[i]] = i
    return []
nums=[1,2,3,4,5,6]
target=8
print(twoSum(nums,target))