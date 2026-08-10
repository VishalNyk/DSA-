# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        head1,head2=list1,list2
        while(head1):
            lst.append(head1.val)
            head1=head1.next
        while(head2):
            lst.append(head2.val)
            head2=head2.next
        if not lst:
            return None
        lst.sort()
        head=ListNode(lst[0])
        curr=head
        for i in lst[1:]:
            curr.next=ListNode(i)
            curr=curr.next
        return head