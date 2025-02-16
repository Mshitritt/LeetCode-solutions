# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for _ in range(n)] for _ in range(m)]
        l, r = 0, n
        t, b = 0, m

        while head and l < r and t < b:
            # top row
            for i in range(l, r):
                if head:
                    mat[t][i] = head.val
                    head = head.next
                else:
                    return mat
            t += 1

            # right column
            for i in range(t, b):
                if head:
                    mat[i][r-1] = head.val
                    head = head.next
                else:
                    return mat
            r -= 1

            # buttom row
            for i in range(r-1, l-1, -1):
                if head:
                    mat[b-1][i] = head.val
                    head = head.next
                else:
                    return mat
            b -= 1

            # left column
            for i in range(b-1, t-1, -1):
                if head:
                    mat[i][l] = head.val
                    head = head.next
                else:
                    return mat
            l += 1
        return mat
