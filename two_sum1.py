class Solution(object): # O(n) EASY
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        items = {}
        for x, y in enumerate(nums):
            diff = target - y
            if diff in items:
                return [items[diff], x]
            items[nums[x]] = x
        
        return [0, 0]
