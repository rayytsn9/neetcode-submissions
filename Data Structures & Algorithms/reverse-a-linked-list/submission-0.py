# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        ptr = head
        temp = []

        while ptr != None:
            temp.append(ptr.val)
            ptr = ptr.next

        temp = temp[::-1]

        print(temp)

        r_head = ListNode(val=temp[0])
        temp_ptr = r_head

        for value in temp[1:]:
            
            r_head.next = ListNode(val=value)
            r_head = r_head.next
            

        return temp_ptr
        