class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = -1
        if numbers[left] + numbers[1] > target:
            return []

        while numbers[left] < numbers[right]:
            
            if numbers[left] + numbers[right] == target:
                return [left + 1, numbers[right]]
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] > target:
                right -= 1
        return []