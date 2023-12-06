from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution
        # returns the comparison of lengths of original list and set of origin list
        return len(set(nums)) != len(nums) 