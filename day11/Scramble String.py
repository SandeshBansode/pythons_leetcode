from collections import Counter
from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        n = len(s1)

        @lru_cache(None)
        def solve(i, j, length):
            a = s1[i:i + length]
            b = s2[j:j + length]

            if a == b:
                return True

            if Counter(a) != Counter(b):
                return False

            for k in range(1, length):
                if solve(i, j, k) and solve(i + k, j + k, length - k):
                    return True

                if solve(i, j + length - k, k) and solve(i + k, j, length - k):
                    return True

            return False

        return solve(0, 0, n)