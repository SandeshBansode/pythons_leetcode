class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []

        def backtrack(start, path):
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]

                if part == part[::-1]:
                    path.append(part)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result