class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res, stack = [], []
    curr = root  # Start from the root node
    
    while curr or stack:  # While there are nodes left to process
        # 1️⃣ Go left as much as possible
        while curr:
            stack.append(curr)  # Push node to stack
            curr = curr.left    # Move left
            
        # 2️⃣ Process the node
        curr = stack.pop()  # Pop from stack (process node)
        res.append(curr.val)  # Store node value
        
        # 3️⃣ Move to the right subtree
        curr = curr.right  

    return res  # Return the final inorder traversal list

# 🔹 Example Usage
if __name__ == "__main__":
    # Constructing the tree
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Running the inorder traversal
    result = inorderTraversal(root)
    print(result)  # Output: [4, 2, 5, 1, 3]
