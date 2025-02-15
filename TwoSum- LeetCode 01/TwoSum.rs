use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut num_to_index = HashMap::new(); // Create a HashMap to store the number and its index

    for (index, &num) in nums.iter().enumerate() {
        let difference = target - num; // Calculate the difference needed to reach the target
        if let Some(&prev_index) = num_to_index.get(&difference) {
            return vec![prev_index as i32, index as i32]; // Return the indices of the two numbers
        }
        num_to_index.insert(num, index); // Add the current number and its index to the HashMap
    }
    vec![] // Return an empty vector if no solution is found (not needed as per problem constraints)
}

fn main() {
    println!("{:?}", two_sum(vec![2, 7, 11, 15], 9)); // Output: [0, 1]
    println!("{:?}", two_sum(vec![3, 2, 4], 6)); // Output: [1, 2]
    println!("{:?}", two_sum(vec![3, 3], 6)); // Output: [0, 1]
}
