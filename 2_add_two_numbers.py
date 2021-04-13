class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return(l2)
        if l2 == None:
            return(l1)
        sum_val = l1.val + l2.val
        if sum_val < 10:
            result = ListNode(sum_val)
            result.next = self.addTwoNumbers(l1.next,l2.next)
            return(result)
        else:
            output = l1.val + l2.val - 10
            result = ListNode(output)
            result.next = self.addTwoNumbers(ListNode(1),self.addTwoNumbers(l1.next,l2.next))
            return(result)
