from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A  # Ensure A is the smaller array

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # Partition index for A
            j = half - i - 2  # Partition index for B

            # Edge cases: -inf when index is out of bounds
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Check if partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # Odd total elements
                    return min(Aright, Bright)
                else:  # Even total elements
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1  # Move left
            else:
                l = i + 1  # Move right

# Example Usage
sol = Solution()
print(sol.findMedianSortedArrays([1,3], [2]))      # Output: 2.00000
print(sol.findMedianSortedArrays([1,2], [3,4]))    # Output: 2.50000
