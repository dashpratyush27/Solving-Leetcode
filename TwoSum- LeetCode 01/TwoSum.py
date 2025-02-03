def two_sum(nums, target):
    num_to_index = {}  # Create a dictionary to store the number and its index
    for index, num in enumerate(nums):
        difference = target - num  # Calculate the difference needed to reach the target
        if difference in num_to_index:  # Check if the difference is in the dictionary
            return [num_to_index[difference], index]  # Return the indices of the two numbers
        num_to_index[num] = index  # Add the current number and its index to the dictionary
    return []  # Return an empty list if no solution is found (not needed as per problem constraints)

# Example usage:
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sum([3, 2, 4], 6))  # Output: [1, 2]
print(two_sum([3, 3], 6))  # Output: [0, 1]
