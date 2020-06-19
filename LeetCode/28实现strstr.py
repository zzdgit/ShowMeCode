class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        num_s = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i: i+num_s] == needle:
                    return i
        return -1