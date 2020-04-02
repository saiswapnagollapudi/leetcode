class Solution(object):
    def sum_of_squares(self,n):
        temp = 0
        while n > 0:
            temp += (n%10)**2
            n = n/10
        n = temp
        return(n)
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n
        while(True):
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(self.sum_of_squares(fast))
            if slow != fast:
                continue
            else:
                break
        return(slow == 1)
