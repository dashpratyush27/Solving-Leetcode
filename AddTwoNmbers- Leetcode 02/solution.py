class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum = val1 + val2 + carry
        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy_head.next

def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Helper function to create a linked list from a list of integers
def create_linked_list(lst):
    dummy_head = ListNode()
    current = dummy_head
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy_head.next

# Test case 1
l1 = create_linked_list([2, 4, 3])  # Represents the number 342
l2 = create_linked_list([5, 6, 4])  # Represents the number 465
result = addTwoNumbers(l1, l2)      # Should represent the number 807
print("Test Case 1 Result:")
print_linked_list(result)           # Expected Output: 7 0 8

# Test case 2
l1 = create_linked_list([0])        # Represents the number 0
l2 = create_linked_list([0])        # Represents the number 0
result = addTwoNumbers(l1, l2)      # Should represent the number 0
print("Test Case 2 Result:")
print_linked_list(result)           # Expected Output: 0

# Test case 3
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])  # Represents the number 9999999
l2 = create_linked_list([9, 9, 9, 9])           # Represents the number 9999
result = addTwoNumbers(l1, l2)                  # Should represent the number 10009998
print("Test Case 3 Result:")
print_linked_list(result)                       # Expected Output: 8 9 9 9 0 0 0 1
