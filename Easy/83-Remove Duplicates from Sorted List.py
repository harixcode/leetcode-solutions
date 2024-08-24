"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    #set pointer to the head of the list
    cur = head
    while cur: #while list is not empty
        while cur.next and cur.next.val == cur.val: #This loop checks if the next node (cur.next) exists and if its value is equal to the current node's value (cur.val). If so, it means there are duplicate values.
            cur.next = cur.next.next
        
        cur = cur.next #set pointer to next value 
    return head 