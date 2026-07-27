class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start_index = 0
        for char in s:
            match_index=t.find(char,start_index)
            if(match_index==-1):
                return False
            start_index=match_index+1
        return True
        