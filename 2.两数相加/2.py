class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        forward = 0
        ret = ListNode()
        tmp = ret
        while l1 or l2 or forward:
            num = 0
            if l1:
                num = l1.val
                l1 = l1.next
            if l2:
                num = num + l2.val
                l2 = l2.next
            forward, num = divmod(num + forward, 10)
            tmp.next = ListNode(num)
            tmp = tmp.next
        return(ret.next)

if __name__ == '__main__':
    sol = Solution()

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    ret = sol.addTwoNumbers(l1, l2)
    while ret:
        print(ret.val, end=' ')
        ret = ret.next
    print('')
