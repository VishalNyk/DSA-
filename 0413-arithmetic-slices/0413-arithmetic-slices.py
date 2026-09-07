class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
            
        total_slices = 0
        current_run = 0
        
        # We start at index 2 because a slice needs at least 3 elements
        for i in range(2, len(nums)):
            # Check if the last three elements form an arithmetic progression
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                # The sequence extends! Increment our running count of new slices
                current_run += 1
                # Add these newly formed slices to our grand total
                total_slices += current_run
            else:
                # The arithmetic sequence broke. Reset the run counter.
                current_run = 0
                
        return total_slices