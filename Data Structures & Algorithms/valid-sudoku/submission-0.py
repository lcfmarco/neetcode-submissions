class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return not self.containDupeRow(board) and not self.containDupeCol(board) and not self.containDupeSquare(board)
        
    def containDupeRow(self, board):
        for row in board:
            rowDupe = set()
            
            for num in row:
                if num in rowDupe:
                    return True
                elif num not in rowDupe and num != ".":
                    rowDupe.add(num)
            
        return False

    def containDupeCol(self, board):
        for i in range(len(board)):
            colDupe = set()
            for row in board:
                if row[i] in colDupe:
                    return True
                elif row[i] not in colDupe and row[i] != ".":
                    colDupe.add(row[i])
        return False

    def containDupeSquare(self, board):
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return True
                    seen.add(board[row][col])
        return False

