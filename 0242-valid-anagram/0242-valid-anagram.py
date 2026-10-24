class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        return True if(collections.Counter(s)==collections.Counter(t)) else False
