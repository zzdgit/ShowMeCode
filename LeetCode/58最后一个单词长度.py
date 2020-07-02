class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_l = [i for i in s.split(' ') if i ]
        if s_l:
            return  len(s_l[-1])
        else:
            return 0