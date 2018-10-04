# You have an array of integers nums and an array queries, where queries[i] is 
# a pair of indices (0-based). Find the sum of the elements in nums from the 
# indices at queries[i][0] to queries[i][1] (inclusive) for each query, then add 
# all of the sums for all the queries together. Return that number modulo 109 + 7.

def sumInRange(nums, queries):
#   modify the list so it reflects the running sum
#   O(n) time to build
    
    for i, v in enumerate(nums):
        if i == 0:
            continue
        
        nums[i] = nums[i-1] + v
        
    result = 0

    # since nums is now the running sum, can use slices to get the query
    # if start of query is 0, then index into the sums at the second index
    # else minus the sum previous to the second query index from the first query index
    
    for query in queries:
        if query[0] == 0:
            result += nums[query[1]]
        else:
            result += nums[query[1]] - nums[query[0] - 1]
            
        
        
    return result % (10 ** 9 + 7)