# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:
        slow, fast = list, list
        size = 0
        head = list

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = fast.next
                while slow != fast:
                    size += 1
                    fast = fast.next
                break
        h1 = math.ceil(size // 2)
        slow = list
        while h1:
            slow = slow.next
            h1 -= 1
        fast = slow.next
        h2Head = slow.next
        slow.next = list
        
        while fast.next != list:
            fast = fast.next
        fast.next = h2Head

        return [slow.next, h2Head]
        
        

        
        # first half head ---> slow
        return []

        

        