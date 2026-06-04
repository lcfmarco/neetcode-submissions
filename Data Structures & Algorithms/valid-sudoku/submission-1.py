class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # All values in this column
        cols = defaultdict(set)
        rows = defaultdict(set)
        # Key = (r // 3, c // 3)
        squares = defaultdict(set)
    

        for r in range(9):
            for c in range(9):
                # If empty, skip it
                if board[r][c] == ".":
                    continue
                
                # Rows is our hash map, r is the key of our current row
                # If this current number we are in is already inside the row hashset, then that means it is a duplicate
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

