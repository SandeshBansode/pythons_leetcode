class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)

        dp = [1] * n
        prev = [-1] * n
        best_len = 1
        best_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            if dp[i] > best_len:
                best_len = dp[i]
                best_idx = i

        result = []

        while best_idx != -1:
            result.append(nums[best_idx])
            best_idx = prev[best_idx]

        return result[::-1]