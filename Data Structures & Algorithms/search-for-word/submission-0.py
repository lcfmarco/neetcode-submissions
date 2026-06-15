class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        used = set()

        def dfs(row_idx, col_idx, pos):
            if row_idx < 0 or row_idx >= rows or col_idx < 0 or col_idx >= cols:
                return False

            if (row_idx, col_idx) in used:
                return False

            if board[row_idx][col_idx] != word[pos]:
                return False

            if pos == len(word) - 1:
                return True

            used.add((row_idx, col_idx))

            found = dfs(row_idx + 1, col_idx, pos + 1) or dfs(row_idx - 1, col_idx, pos + 1) or dfs(row_idx, col_idx + 1, pos + 1) or dfs(row_idx, col_idx - 1, pos + 1)

            used.remove((row_idx, col_idx))

            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False

        