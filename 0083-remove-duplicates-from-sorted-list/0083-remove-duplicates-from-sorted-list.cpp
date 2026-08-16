/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy=head;
        ListNode* ptr=head;
        ListNode* ans=dummy;
        while(head && head->next){
            if(head->next && head->next->val==head->val){
                ptr=head;
                while(ptr->next && ptr->next->val==head->val){
                    ptr=ptr->next;
                }
                head=ptr->next;
            }else{
                head=head->next;
            }
            dummy->next=head;
            dummy=dummy->next;
        }
        return ans;
    }
};