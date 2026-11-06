class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if(len(intervals)<=1):
            return intervals
        
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]

        for i in range(1,len(intervals)):
            cstart,cend=intervals[i]
            lend=res[-1][1]
            if(cstart<=lend):
                res[-1][1]=max(cend,lend)
            else:
                res.append(intervals[i])
        return res