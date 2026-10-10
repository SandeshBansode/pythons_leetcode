class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(path, opened, closed):
            if len(path) == 2 * n:
                result.append(path)
                return

            if opened < n:
                backtrack(path + "(", opened + 1, closed)

            if closed < opened:
                backtrack(path + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return result