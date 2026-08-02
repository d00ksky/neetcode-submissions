class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted([letter for letter in s], key=lambda letter: letter)
        sorted_t = sorted([letter for letter in t], key=lambda letter: letter)

        if sorted_s == sorted_t:
            return True
        return False