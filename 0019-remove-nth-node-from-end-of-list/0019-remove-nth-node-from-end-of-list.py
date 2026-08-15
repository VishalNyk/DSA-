# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        l=0
        curr=head
        while curr:
            curr=curr.next
            l+=1
        print(l)
        index=l-n # the node whose next element to be deleted
        prev=dummy
        for i in range(0,index):
            prev=prev.next
        prev.next=prev.next.next

        temp=dummy               # delete 0  or instead of 3 line , return dummy.next
        dummy=dummy.next
        temp=None

        return dummy

        

