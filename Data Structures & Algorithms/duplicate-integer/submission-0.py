class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for number in nums:
            count = nums.count(number)
            if count > 1:
                return True
        return False