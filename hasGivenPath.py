# Given a binary tree t and an integer s, determine whether there is a 
# root to leaf path in t such that the sum of vertex values equals s.

def hasPathWithGivenSum(t, s):
    if t == None:
        return s == 0
    
    if t.value == s and not t.left and not t.right:
        return True
    
    left = False
    right = False
    
    if t.left:
        left = hasPathWithGivenSum(t.left, s - t.value)
        
    if t.right:
        right = hasPathWithGivenSum(t.right, s - t.value)
    
    return left or right