# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head
        curr=head
        length=1
        while curr.next:
            curr=curr.next
            length+=1
        curr.next=head  # list is made circular

        point=length- k%length
        turr=head
        for i in range(point-1):
            turr=turr.next
        newhead=turr.next
        turr.next=None

        return newhead

        
