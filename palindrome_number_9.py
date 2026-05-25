class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        """
        new_num = [y for y in str(x)] #lowest runtime: 4ms highest runtime: 24ms
        new_num.reverse() O(n)

        if ''.join(new_num) == str(x):
            return True
        else:
            return False
        """
        
        length = abs(x) # EASY lowest runtime: 3ms highest runtime: 18ms
        reversed = 0
        while length > 0: # O(log n) in some edge cases, O(n) in average complexity
            number = length % 10
            reversed = (reversed * 10) + number
            length //= 10
        
        if reversed == x:
            return True
        return False
        
        
       
        
