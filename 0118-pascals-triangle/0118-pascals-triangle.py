class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        num = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return num
        elif numRows == 0:
            return []
        
        row = []
        for i in range(2, numRows):
            for j in range(i - 1):
                row.append(sum(num[-1][j:j + 2]))
            num.append([1] + row + [1])
            row = []

        return num