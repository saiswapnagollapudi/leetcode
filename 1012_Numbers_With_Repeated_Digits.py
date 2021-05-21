class Solution:
    def numDupDigitsAtMostN(self, N):
        res = 0
        length = len(str(N+1))
        def A(m, n):
            return 1 if n == 0 else A(m, n - 1) * (m - n + 1)
        #calculating number of numbers without any repeating characters with lengths upto length-1
        for i in range(1, length): 
            res += 9 * A(9, i - 1)   
        s = set()
        #if input is 1234 fixing each digit find number of possible numbers with non repeating 
        #digits 1XXX second digit can be 0 leading to 8*7 possible numbers
        for i,x in enumerate(str(N+1)):
            #if there is a repeating digit dont count
            if len(str(N)[:i]) != len(set(str(N)[:i])):
                break
            #if the first digit is 1 continue
            if i == 0 and int(x) == 1:
                s.add(x)
                continue
            for j in range(0,int(x)):
                if j in s:
                    continue
                if i == 0 and j == 0:
                    continue
                if str(j) in s:
                    continue
                res += A(9-i, length - i - 1)
            s.add(x)
        return N - res 
        
