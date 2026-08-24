class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            flage=True
            for j in range(len(nums)):
                if i!=j and nums[i]==nums[j]:
                    flage=False
                    break
            if flage:
                return nums[i]