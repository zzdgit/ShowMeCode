# coding: utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def juge(new_s):
            s_s = new_s[::-1]
            if s_s == new_s:
                return True
            else:
                return False
        if len(s) < 2:
            return s
        l_s = ''
        for i in range(len(s)):
            for j in range(i):
                if i + j + 1 > i:
                    continue
                flag1 = juge(s[i:i+j+1])
                flag2 = juge(s[i-j-1:i+j+1])
                
                if flag1 :
                    l_s = s[i:i+j+1]
                elif flag2:
                    l_s = s[i-j-1:i+j+1]
                else:
                    continue
        return l_s
                
            