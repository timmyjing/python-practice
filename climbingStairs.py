# You are climbing a staircase that has n steps. 
# You can take the steps either 1 or 2 at a time. 
# Calculate how many distinct ways you can climb to the top of the staircase.
def climbingStairs(n):
    steps = [0] * n
    
    for i in range(n):
        for step in range(1,3):
            if (i + 1) - step == 0:
                steps[i] += 1
            elif (i + 1) - step > 0:
                steps[i] += steps[i - step]
            
    
    
    
    
    return steps[n - 1]
