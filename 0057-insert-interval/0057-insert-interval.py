class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res=[]

        for i in range(len(intervals)):
            if(intervals[i][1]<newInterval[0]): #does currentInterval ends before newInterval
                res.append(intervals[i])
            elif(intervals[i][0]>newInterval[1]): # does currentInterval starts after newInterval
                res.append(newInterval)
                return res+intervals[i:] 
            else:
                newInterval[0]=min(newInterval[0],intervals[i][0])
                newInterval[1]=max(newInterval[1],intervals[i][1])
        res.append(newInterval)

        return res
                