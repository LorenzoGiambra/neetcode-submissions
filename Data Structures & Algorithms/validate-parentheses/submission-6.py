class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        pairs = {
                "}": "{",
                ")": "(",
                "]": "["
                }
        chars = []
        for i in range(len(s)):
            if s[i] in pairs.values():
                chars.append(s[i])
            elif s[i] in pairs.keys():
                if not chars or pairs[s[i]] != chars[-1]:
                    return False
                chars.pop()
        #if len(chars) != 0:
        #    return False
        #return True
        return not chars

