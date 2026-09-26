class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        n=len(y)
        l,r=0,n-1
        pal=True
        while l<r:
            if y[l]!=y[r]:
                pal=False
                break
            l+=1
            r-=1
        return pal
