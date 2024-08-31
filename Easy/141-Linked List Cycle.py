

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        Approach
        initialise fast and slow pointer to head. 
        fast point will not reach the end of linked list if there exist a cycle. 
        fast and slow pointers will meet at some point if there is a cycle. 
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    """
    O(n)
    """