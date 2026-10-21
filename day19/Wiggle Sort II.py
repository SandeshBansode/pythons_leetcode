class Solution:
    def wiggleSort(self, nums):
        ordered = sorted(nums)
        mid = (len(nums) + 1) // 2

        nums[::2] = ordered[:mid][::-1]
        nums[1::2] = ordered[mid:][::-1]