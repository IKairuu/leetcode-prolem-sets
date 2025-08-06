class Solution(object):
    def __init__(self):
        self.stack = []
        
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        valid = "()[]{}"
        mapping = {')':'(', ']':'[', '}':'{'}

        for index, char in enumerate(s):
            self.stack.append(char)

            #checking the next input
            for index2, items in enumerate(valid):
                if items == char:
                    if index2 % 2 != 0:
                        for mapp in mapping.keys():
                            if mapp == char and mapping[mapp] == self.stack[len(self.stack)-2]:
                                self.stack.pop(len(self.stack)-1)
                                self.stack.pop(len(self.stack)-1)
        
        if len(self.stack) == 0:
            return True
        else:
            return False

        


            



        
