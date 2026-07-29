class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i in range(len(numbers)):
            complement=(target-numbers[i])
            if complement in seen:
                return [seen[complement]+1,i+1]
            seen[numbers[i]]=i
        return [0,0]
