class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(1, n):
            result = []
            i = 0

            while i < len(s):
                j = i + 1

                while j < len(s) and s[j] == s[i]:
                    j += 1

                result.append(str(j - i))
                result.append(s[i])
                i = j

            s = "".join(result)

        return s