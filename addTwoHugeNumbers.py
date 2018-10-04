# You're given 2 huge integers represented by linked lists. 
# Each linked list element is a number from 0 to 9999 that represents 
# a number with exactly 4 digits. The represented number might have leading 
# zeros. Your task is to add up these huge integers and return the result in the same format.


# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
#   could traverse both lists first and build values then add them up
#   could also traverse each list til the end and keep track of the prev for each and add them up
#   break off the tail node each time until one of the lists is empty
#   dont forget to carry
 
    numA = []
    numB = []
    
    while a:
        numA.append(a.value)
        a = a.next
    
    while b:
        numB.append(b.value)
        b = b.next
    
    print(numA)
    print(numB)
    
    result = None
    carry = 0
    
    while numA and numB:
        val = numA.pop(-1) + numB.pop(-1) + carry
        carry = val // 10000
        node = ListNode(val % 10000)
        
        node.next = result
        result = node
        
    
    rest = None
    
    if numA:
        rest = numA
    
    if numB:
        rest = numB
        
    while rest:
        val = rest.pop(-1) + carry
        carry = val // 10000
        node = ListNode(val % 10000)
        
        node.next = result
        result = node
        
    
    if carry:
        node = ListNode(carry)
        
        node.next = result
        result = node
    
    
    return result
