class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        
        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1] + 1:
                prefix_sum += nums[j]
            else:
                break
        num_set = set(nums)
        while prefix_sum in num_set:
            prefix_sum += 1
            
        return prefix_sum
