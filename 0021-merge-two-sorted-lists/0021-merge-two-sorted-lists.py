# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val <= list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
        elif list1:
            head = list1
            list1 = list1.next
        elif list2:
            head = list2
            list2 = list2.next
        else:
            return None

        curr = head
        head.next = None
        while list1 or list2:
            #val1 = list1.val
            #val2 = list2.val
            if list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next
                    curr.next = None
                else:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next
                    curr.next = None
            elif list1:
                curr.next = list1
                list1 = None
            else:
                curr.next = list2
                list2 = None

        return head

