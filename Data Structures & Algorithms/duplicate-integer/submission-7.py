class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        find=set()
        for num in nums:
            if num in find:
                return True
            find.add(num)
        return False
        
        