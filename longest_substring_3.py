class Solution(object):
    def lengthOfLongestSubstring(self, s): # O(n^2) can still be improved using dictionary MEDIUM
        """
        :type s: str
        :rtype: int
        """
        subs = []
        highest = 0
        for x in range(len(s)):
            current = []
            if s[x:x+95] == s[x+95:x+(95+95)]:
                continue
            else:
                for y in s[x:]:
                    if y in current:
                        if len(current) > highest:
                            highest = len(current)
                        subs.append(current)
                        current = []
                               
                    current.append(y)
            if highest < len(current):
                highest = len(current)
            subs.append(current)
        return highest
            


        
