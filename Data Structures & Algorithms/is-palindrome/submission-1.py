class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_characters = []
        for ch in s:
            if ch.isalnum():
                cleaned_characters.append(ch.lower())
        cleaned_string = "".join(cleaned_characters)
        return cleaned_string == cleaned_string[::-1]

        