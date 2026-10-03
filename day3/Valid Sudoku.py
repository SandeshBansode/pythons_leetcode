class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                box = (i // 3) * 3 + (j // 3)

                if value in rows[i]:
                    return False

                if value in cols[j]:
                    return False

                if value in boxes[box]:
                    return False

                rows[i].add(value)
                cols[j].add(value)
                boxes[box].add(value)

        return True