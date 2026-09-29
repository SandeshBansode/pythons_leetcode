class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:

            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            # Boundary values
            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == m else nums1[i]

            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == n else nums2[j]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total length
                return (max(left1, left2) +
                        min(right1, right2)) / 2

            # nums1 partition is too far right
            elif left1 > right2:
                high = i - 1

            # nums1 partition is too far left
            else:
                low = i + 1