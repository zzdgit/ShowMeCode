class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        dic = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',
               'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l',
               'M':'m', 'N':'n', 'O':'o','P':'p', 'Q':'q', 'R':'r',
               'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x',
               'Y':'y', 'Z':'z'}
        n_s = ''
        for i in str:
            if dic.get(i, None):
                n_s = n_s + dic.get(i)
            else:
                n_s = n_s + i
        return n_s