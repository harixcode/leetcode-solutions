class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates( head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur = head
    while cur: #while list is not empty
        while cur.next and cur.next.val == cur.val: #This loop checks if the next node (cur.next) exists and if its value is equal to the current node's value (cur.val). If so, it means there are duplicate values.
            cur.next = cur.next.next
        
        cur = cur.next #set pointer to next value 
    return head

if __name__ == "__main__":
    head = [1,1,1,2,3]
    for i in head:
        x = ListNode(i)
        x = x.next 
    ans = deleteDuplicates(x)
    print (ans)