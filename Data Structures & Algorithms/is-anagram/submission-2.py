class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s=set()
        set_t=set()
        if len(s)!=len(t):
            return False

        return sorted(s)==sorted(t)