class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1=m-1
        p2=n-1 # last position of valid elements in nums1 and num2
        p=m+n-1 # last position of valid element in nums1 after merging

        # set big elements at last position as we are starting from the largest elements only
        while(p1>=0) and (p2>=0):  
            if(nums1[p1]>nums2[p2]):
                nums1[p]=nums1[p1]
                p1=p1-1
            else:
                nums1[p]=nums2[p2]
                p2=p2-1
            p=p-1
        
        # add if remaining elements are still there
        nums1[:p2+1]=nums2[:p2+1]