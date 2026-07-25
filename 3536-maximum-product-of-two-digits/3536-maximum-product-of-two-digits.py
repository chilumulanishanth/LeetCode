class Solution:
    def maxProduct(self, n: int) -> int:
        digits=[]
        val=1
        while n>0:
            digits.append(n%10)
            n=n//10
        digits.reverse()
        digits.sort()
        n=len(digits)-1
        for i in range(n,n-2,-1):
            val=val*digits[i]
        return val
             