class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_string = ''
        for word in strs:
            l = len(word)
            enc_string = enc_string + str(l) + '#' + word
        return enc_string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j + 1:j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res
            
