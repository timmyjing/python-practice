# Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. 
# The subarray from which this sum comes must contain at least 1 element.


def arrayMaxConsecutiveSum2(inputArray):
    maxSum = inputArray.pop(0)
    currSum = maxSum
    
    for i in inputArray:
        if i + currSum > i:
            currSum += i
        else:
            currSum = i
        maxSum = max(maxSum, currSum)
    maxSum = max(maxSum, currSum)
        
    return maxSum
    