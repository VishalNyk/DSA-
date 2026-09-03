class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # ws=10
        # ans=[]
        # for i in range(len(s)-ws):
        #     if(s[i:ws+i] in s[i+1:len(s)]):   
        #         ans.append(s[i:ws+i])
        
        # return list(set(ans))

        from collections import Counter
        ans=[]

        seq_count=Counter()
        for i in range(len(s)-9):
            cs=s[i:i+10]
            seq_count[cs]+=1

            if(seq_count[cs]==2):
                ans.append(cs)
        return ans
        