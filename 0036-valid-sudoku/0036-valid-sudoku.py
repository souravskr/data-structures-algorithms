class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenSet = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    preLen = len(seenSet)
                    seenSet.add(f'{board[i][j]} found at row[{i}]')
                    seenSet.add(f'{board[i][j]} found at column[{j}]')
                    seenSet.add(f'{board[i][j]} found at box[{i//3}][{j//3}]')
                    if preLen != len(seenSet) - 3:
                        return False
        return True