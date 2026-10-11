class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                p1 = i + j
                p2 = i + j + 1

                product = (
                    (ord(num1[i]) - ord('0')) *
                    (ord(num2[j]) - ord('0')) +
                    result[p2]
                )

                result[p2] = product % 10
                result[p1] += product // 10

        return ''.join(str(d) for d in result).lstrip('0') or '0'