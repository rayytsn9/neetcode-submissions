class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for index, n in enumerate(nums):

            rem = target - n

            if rem in seen:
                return [seen[rem], index]

            seen[n] = index
