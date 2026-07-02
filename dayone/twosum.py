class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]

            num_map[num] = i

# Example
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))