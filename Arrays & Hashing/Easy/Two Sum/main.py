from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in hash_dict:
                return [hash_dict[complement], i]
            hash_dict[n] = i