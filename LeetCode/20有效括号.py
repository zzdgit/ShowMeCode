# coding = utf-8

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        str_l = ['{', '(', '[']
        str_r = ['}', ')', ']']
        s_dict = {'}': '{', ')': '(', ']': '['}
        for i in s:
            if i in str_l:
                stack.append(i)
            elif i in str_r and stack:
                r_str = s_dict.get(i)
                if r_str == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            elif i in str_r and not stack:
                return False
            else:
                pass
        if stack:
            return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().isValid("[([]])"))
