class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if i < target:
                print(f"i={nums[i]}")
                for j in range(len(nums))[i:]:
                    print(f"j={nums[j]}")
                    if nums[i] + nums[j] == target and i != j:
                        return [i, j]

            

