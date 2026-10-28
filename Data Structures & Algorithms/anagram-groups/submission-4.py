class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for ch in strs:
            key=''.join(sorted(ch))
            if key not in dict:
                dict[key]=[]
            dict[key].append(ch)
        return list(dict.values())



