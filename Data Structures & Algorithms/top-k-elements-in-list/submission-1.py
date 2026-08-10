class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_count = {}

        for num in nums:
            if num not in int_count:
                int_count[num] = 0
            
            int_count[num] += 1
        sorted_count = sorted(int_count.items(), key=lambda num: num[1], reverse=True)
        return [count[0] for count in sorted_count][:k] 