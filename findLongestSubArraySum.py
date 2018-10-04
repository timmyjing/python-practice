
# You have an unsorted array arr of non-negative integers and a number s. Find a longest contiguous subarray in arr that has a sum equal to s. Return two integers that represent its inclusive bounds. If there are several possible answers, return the one with the smallest left bound. If there are no answers, return [-1].

# Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.

def findLongestSubarrayBySum(s, arr):
    result = None
    
    sumSoFar = 0
    start = 0
    end = 0
    
    for i, num in enumerate(arr):
        sumSoFar += num
        end = i
        
#         add each number to the consec sum
#         
#         if sum is over s, then keep sliding window over until it isn't
        while sumSoFar > s:          
            sumSoFar -= arr[start]
            start += 1
            
#             check if sum is now s, if so, update the index
        if sumSoFar == s:
            if result == None or (end - start > result[1] - result[0]):
                result = [start, end]


    if result == None:
        return [-1]
        
    result[0] += 1
    result[1] += 1
    
    return result
    
    
# keep a start index, keep building until greater than or equal to s
# if equal to s set the new result
# if greater than s, slide the window one at the start over by one
# 