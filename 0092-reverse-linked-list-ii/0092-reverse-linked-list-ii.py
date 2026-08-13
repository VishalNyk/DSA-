# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst=[]
        curr=head
        while(curr):
            lst.append(curr.val)
            curr=curr.next
        lst[left-1:right]=lst[left-1:right][::-1]
        i=0
        print(lst)
        turr=head
        while turr and i<len(lst):
            turr.val=lst[i]
            turr=turr.next
            i+=1
        return head