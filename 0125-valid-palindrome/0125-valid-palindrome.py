class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s="".join(c for c in s if(c.isalpha()==True or c.isalnum()==True)).lower()
        return s==s[::-1]
        