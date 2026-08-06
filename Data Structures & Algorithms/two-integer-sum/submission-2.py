class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if i < target:
                print(nums[i])
                for j in range(len(nums))[i:]:
                    print(nums[j])
                    if nums[i] + nums[j] == target and nums[i] != nums[j]:
                        return [i, j]

            

