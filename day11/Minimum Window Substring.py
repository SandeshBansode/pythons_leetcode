from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = Counter()

        required = len(t)
        formed = 0
        left = 0

        best_start = 0
        best_len = float("inf")

        for right, ch in enumerate(s):
            window[ch] += 1

            if ch in need and window[ch] <= need[ch]:
                formed += 1

            while formed == required:
                current_len = right - left + 1

                if current_len < best_len:
                    best_len = current_len
                    best_start = left

                left_char = s[left]

                if left_char in need:
                    if window[left_char] == need[left_char]:
                        formed -= 1

                    window[left_char] -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]