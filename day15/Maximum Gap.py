class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        minimum = min(nums)
        maximum = max(nums)

        if minimum == maximum:
            return 0

        size = max(1, (maximum - minimum + n - 2) // (n - 1))
        bucket_count = (maximum - minimum) // size + 1

        bucket_min = [float("inf")] * bucket_count
        bucket_max = [float("-inf")] * bucket_count

        for num in nums:
            index = (num - minimum) // size
            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)

        best = 0
        prev_max = minimum

        for i in range(bucket_count):
            if bucket_min[i] == float("inf"):
                continue

            best = max(best, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return best