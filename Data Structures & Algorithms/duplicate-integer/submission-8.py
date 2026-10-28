class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sat=set()
        for num in nums:
            if num in sat:
                return True
            sat.add(num)
        return False
            