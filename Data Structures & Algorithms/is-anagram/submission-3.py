class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if s.count(char) != t.count(char):
                return False
        for char in t:
            if s.count(char) != t.count(char):
                return False
        return True

        