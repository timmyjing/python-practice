# Given a singly linked list of integers, 
# determine whether or not it's a palindrome.

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    vals = []
    
    curr = l
    
    while curr:
        vals.append(curr.value)
        curr = curr.next
        
    mid = len(vals) // 2
    
    if len(vals)%2==0:
        return vals[:mid] == vals[-1:mid-1:-1]
    else:
        return vals[:mid] == vals[-1:mid:-1]
        
