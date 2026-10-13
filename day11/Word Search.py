class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        def dfs(r, c, k):
            if k == len(word):
                return True

            if r < 0 or r >= m or c < 0 or c >= n:
                return False

            if board[r][c] != word[k]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, k + 1) or
                dfs(r - 1, c, k + 1) or
                dfs(r, c + 1, k + 1) or
                dfs(r, c - 1, k + 1)
            )

            board[r][c] = temp
            return found

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False