# Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.




# determine if there is a consec range
# if new number is consec, add to running range
# if not start a new range

def composeRanges(nums):
    
    if not nums:
        return []
    
    result = []
    start = nums.pop(0)
    end = start
    
    for num in nums:
        if num == end + 1:
            end += 1
        else:
            r = str(start)
            if end != start:
                r += "->" + str(end)
            result.append(r)
            start = num
            end = num
            
    r = str(start)
    if end != start:
        r += "->" + str(end)
    result.append(r)
            
    return result
