class Solution(object): #MEDIUM 7ms
  """
  can still be improved if I implemented a reusable functions to reduce runtime
  """
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        index = -1

        if s == "" or (s[0].isdigit() is False and s[0] != " " and s[0] != "-" and s[0] != "+"):
            return 0

        for x in s:
            if x != " ":
                if x.isdigit() is False and x != "-" and x != "+":
                    break

                if index >= 0:
                    if x.isdigit() is False:
                        break

                    if stack[index] == "-" and x == "0":
                        continue
                    stack.append(x)
                    index += 1
                else:
                    stack.append(x)
                    index += 1
            
            
            if x == " " and index >= 0:
                joined = ''.join(stack)
                if joined.isdigit() is True or (joined.startswith("-") and joined[1:].isdigit()):
                    return int(''.join(stack))
                return 0
            
        joined = ''.join(stack)
        if joined.isdigit() is False and not ((joined.startswith("-") and joined[1:].isdigit()) or (joined.startswith("+") and joined[1:].isdigit())):
            return 0
            
        answer = int(joined)
        if abs(answer) >= pow(2, 31):
            if str(answer)[0] == "-":
                return (-1 * pow(2, 31))
            else:
                return (pow(2, 31)) - 1

        return answer
        
