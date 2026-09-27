class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict={}

        for ch in s:
            dict[ch]=dict.get(ch,0)+1
        for chr in t:
            dict[chr]=dict.get(chr,0)-1
        for dicts in dict:
            if dict[dicts]!=0:
                return False
        return True
        ''
            


        
