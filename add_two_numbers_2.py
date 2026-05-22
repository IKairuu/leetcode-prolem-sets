# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2): #MEDIUM
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_l1 = []
        new_l2 = []
        first = l1
        while(first != None):
            new_l1.append(first.val)
            first = first.next
        sec = l2
        while(sec != None):
            new_l2.append(sec.val)
            sec = sec.next
        new_l1.reverse()
        new_l2.reverse()    
        answer = int("".join([str(x) for x in new_l1])) + int("".join(str(x) for x in new_l2))
        answer_list = [int(x) for x in str(answer)]
        answer_list.reverse()
        prev = None
        head = None
        for y, x in enumerate(answer_list):
            new_node = ListNode(x)
            if y == 0:
                head = new_node
            if prev != None:
                prev.next = new_node
            prev = new_node
        return head

        
