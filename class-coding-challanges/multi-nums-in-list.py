class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for num1 in nums:
            for num2 in nums:
                if num1 == num2:
                    return True
        return False
