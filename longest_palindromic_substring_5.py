class Solution(object):  # MEDIUM 
  """ 
  can still be improved by using one for loop and checking the right 
  and left side substring for palindrome reducing the load of accessing 
  each elements per N
  """
    def  check_palindrome(self,  string):
        left,  right = 0, len(string) - 1
        while left  < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 1:
            return s

        if self.check_palindrome(s):
            return s

        palindromic  = []
        for x in range(len(s)):
            current = ""
            for y in range(x, len(s)):
                current += s[y]
                if self.check_palindrome(current) and current != "":
                    palindromic.append(current)

        maximum = max(palindromic, key=len)

        return  maximum

        

        
