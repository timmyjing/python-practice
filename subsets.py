# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#       base case
        if not nums:
            return [[]]
        
        el = nums.pop(-1)
    
        prev = self.subsets(nums)
        rest = []
        for x in prev:
            new = x[:]
            new.append(el)
            rest.append(new)
        
        
        print(prev)
        print(rest)
        
        return prev + rest
        

#   = [[]]
#  1 = [[],[1]]
#  1,2 = [[], [1], [2], [1,2]]
#  1,2,3 = [[],[1],[2],[1,2], [3],[1,3],[2,3],[1,2,3]]