class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            remaining = len(s) - start
            segments_left = 4 - len(parts)

            if remaining < segments_left or remaining > 3 * segments_left:
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                if len(part) > 1 and part[0] == "0":
                    break

                if int(part) > 255:
                    continue

                backtrack(start + length, parts + [part])

        backtrack(0, [])
        return result