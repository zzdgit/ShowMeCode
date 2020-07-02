class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n_list = []
        s_list = s.split(' ')
        for i in s_list:
            n_list.append(i[::-1])
        return ' '.join(n_list)