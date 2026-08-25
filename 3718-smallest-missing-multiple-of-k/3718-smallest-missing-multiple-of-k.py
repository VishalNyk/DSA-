from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Convert to a set for O(1) lookups
        num_set = set(nums)
        
        i = 1
        while True:
            prd = k * i
            if prd not in num_set:
                return prd
            i += 1
