class Solution(object): #MEDIUM O(n)
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        subs = [[] for x in range(numRows)]
        string = ""
        index = 0
        shift = False
        if numRows == 1:
            return s
        else:
            for x in s:
                subs[index].append(x)
                if not shift:
                    index += 1
                else:
                    index -= 1
                
            
                if index == numRows-1:
                    shift = True

                if index == 0:
                    shift = False

  
        for x in subs:
            string += ''.join(x)

        return string



        
