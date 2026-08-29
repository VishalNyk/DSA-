class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if(len(s)==1):
            return 1
        rev=s[::-1].strip()
        i,l=0,0
        while(i<len(rev) and rev[i]!=' '):
            i+=1
            l+=1
        return l

        