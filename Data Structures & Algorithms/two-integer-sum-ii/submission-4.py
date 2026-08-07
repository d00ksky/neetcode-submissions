class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = numbers[0]
        right = numbers[-1]

        if left + numbers[1] > target:
            print(left, numbers[1])
            return []

        while left < right:
            print(f"left={left}, right={right}")
            if left + right == target:
                print([left, right])
                return [left, right] 
            if left + right < target:
                left += 1
            if left + right > target:
                right -= 1
        return []