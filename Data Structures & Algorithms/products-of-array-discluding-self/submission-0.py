class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1] 

        for j in range(len(nums) -2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]

        for k in range(len(nums)):
            answer.append(left[k] * right[k])

        return answer



            
        