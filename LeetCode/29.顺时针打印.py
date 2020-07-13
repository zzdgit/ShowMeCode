class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return self.test([], matrix)
    
    def test(self, l , matrix):
        if not matrix:
            return l
        if len(matrix) < 2:
            l = l + matrix.pop()
        if len(matrix) == 2:
            tmp = matrix.pop()[::-1]
            l = l + matrix.pop(0) + tmp
        if len(matrix) > 2:
            l = l + matrix.pop(0)
            tmp = matrix.pop()[::-1]
            for i in matrix:
                if i:
                    l.append(i.pop())
                else:
                    matrix.remove(i)
            l = l + tmp
            le = len(matrix) - 1
            for j in range(le):
                if matrix[le-j]:
                    l.append(matrix[le-j].pop(0))
                else:
                    matrix.pop(le-j)
        return self.test(l, matrix)
        
a = [[1,2,3],[4,5,6],[7,8,9]]
a= [[3],[2]]
a= [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
a= [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
print(Solution().spiralOrder(a))