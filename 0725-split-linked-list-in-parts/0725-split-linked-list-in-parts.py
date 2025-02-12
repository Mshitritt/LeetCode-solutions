# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if k == 1:
            return [head]
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        res = [None] * k
        extra = 0 if size <= k else size % k
        base = max(1, size // k)
        i_res = 0

        curr = head
        while curr:
            total = base
            if extra:
                total += 1
                extra -= 1
            
            res[i_res] = curr
            prev = curr
            while curr and total:
                prev = curr
                curr = curr.next
                total -= 1
            if not curr:
                return res
            prev.next = None
            i_res += 1
        return res

            


        
        
                


            

