class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    value = board[r][c]
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[(r // 3) * 3 + c // 3].add(value)

        def solve(pos):
            if pos == len(empty):
                return True

            best = pos
            best_options = None

            for i in range(pos, len(empty)):
                r, c = empty[i]
                box = (r // 3) * 3 + c // 3

                options = [
                    num for num in "123456789"
                    if num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[box]
                ]

                if best_options is None or len(options) < len(best_options):
                    best = i
                    best_options = options

                if len(options) == 1:
                    break

            if not best_options:
                return False

            empty[pos], empty[best] = empty[best], empty[pos]

            r, c = empty[pos]
            box = (r // 3) * 3 + c // 3

            for num in best_options:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if solve(pos + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            empty[pos], empty[best] = empty[best], empty[pos]

            return False

        solve(0)