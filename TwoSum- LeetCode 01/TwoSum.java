import java.util.HashMap;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numToIndex = new HashMap<>();  // Create a HashMap to store the number and its index
        
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];  // Calculate the difference needed to reach the target
            if (numToIndex.containsKey(difference)) {  // Check if the difference is in the HashMap
                return new int[] { numToIndex.get(difference), i };  // Return the indices of the two numbers
            }
            numToIndex.put(nums[i], i);  // Add the current number and its index to the HashMap
        }
        
        // Return an empty array if no solution is found (not needed as per problem constraints)
        return new int[] {};
    }

    public static void main(String[] args) {
        // Example usage:
        int[] result1 = twoSum(new int[] {2, 7, 11, 15}, 9);
        System.out.println("Output: [" + result1[0] + ", " + result1[1] + "]");  // Output: [0, 1]
        
        int[] result2 = twoSum(new int[] {3, 2, 4}, 6);
        System.out.println("Output: [" + result2[0] + ", " + result2[1] + "]");  // Output: [1, 2]
        
        int[] result3 = twoSum(new int[] {3, 3}, 6);
        System.out.println("Output: [" + result3[0] + ", " + result3[1] + "]");  // Output: [0, 1]
    }
}
