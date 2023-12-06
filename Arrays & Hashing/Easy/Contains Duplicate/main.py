from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution
        # a `hash_set` which will keep record of already present elements
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            else:
                hash_set.add(n)
        return False