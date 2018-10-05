# You are planning to rob houses on a specific street, and you know that every house on the street 
# has a certain amount of money hidden. The only thing stopping you from robbing all of them in one night 
# is that adjacent houses on the street have a connected security system. The system will automatically 
# trigger an alarm if two adjacent houses are broken into on the same night.

# Given a list of non-negative integers nums representing the amount of money hidden in each house, 
# determine the maximum amount of money you can rob in one night without triggering an alarm.

def houseRobber(nums):
  if not nums:
    return 0
  
  cache = [0, 0]
  
  for num in nums:
    cache[0], cache[1] = cache[1], max(num + cache[0], cache[1])
    
  return cache[1]