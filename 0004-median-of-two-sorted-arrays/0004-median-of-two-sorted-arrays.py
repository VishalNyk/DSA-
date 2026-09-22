class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always binary search on the smaller array to minimize the search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            # Find the edge values around the cuts, using infinity for out-of-bounds
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # Check if we have found the perfect partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Even total length: average of the max lefts and min rights
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                # Odd total length: the max of the left side is the median
                else:
                    return float(max(maxLeftX, maxLeftY))
            
            # We are too far right on nums1; move left
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # We are too far left on nums1; move right
            else:
                low = partitionX + 1