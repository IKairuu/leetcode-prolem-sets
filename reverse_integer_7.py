class Solution(object): #MEDIUM 7ms
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if len(str(x)) <= 1:
            return x
        

        string = [y for y in str(x)]
        
        string.reverse()
        while string[0] == "0":
            string.pop(0)

        if string[len(string)-1] == "-":
            string.pop(len(string)-1)
            string.insert(0, "-")

        new_string = ''.join(string)
        new_num = long(new_string)

        if abs(new_num) >= 2147483651:
            return 0

        return new_num
        
