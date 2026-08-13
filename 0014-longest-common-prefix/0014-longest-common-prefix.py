class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first,last=strs[0],strs[-1]
        i=0
        prefix=""
        for c1,c2 in zip(first,last):
            if(c1==c2):
                prefix+=c1
            else:
                break
        return prefix
