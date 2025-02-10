class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1, B = nums2;
        int total = A.length + B.length;
        int half = total / 2;

        if (A.length > B.length) {
            int[] temp = A;
            A = B;
            B = temp;  // Ensure A is the smaller array
        }

        int l = 0, r = A.length - 1;
        while (true) {
            int i = (l + r) / 2;  // Partition index for A
            int j = half - i - 2;  // Partition index for B

            int Aleft = (i >= 0) ? A[i] : Integer.MIN_VALUE;
            int Aright = (i + 1 < A.length) ? A[i + 1] : Integer.MAX_VALUE;
            int Bleft = (j >= 0) ? B[j] : Integer.MIN_VALUE;
            int Bright = (j + 1 < B.length) ? B[j + 1] : Integer.MAX_VALUE;

            if (Aleft <= Bright && Bleft <= Aright) {
                if (total % 2 == 1) {  // Odd total elements
                    return Math.min(Aright, Bright);
                } else {  // Even total elements
                    return (Math.max(Aleft, Bleft) + Math.min(Aright, Bright)) / 2.0;
                }
            } else if (Aleft > Bright) {
                r = i - 1;  // Move left
            } else {
                l = i + 1;  // Move right
            }
        }
    }

    // Example Usage
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.findMedianSortedArrays(new int[]{1, 3}, new int[]{2}));    // Output: 2.00000
        System.out.println(sol.findMedianSortedArrays(new int[]{1, 2}, new int[]{3, 4}));  // Output: 2.50000
    }
}