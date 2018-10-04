# Given a Linked List, remove nodes that have the value k.

def removeKFromList(l, k):
    
    curr = l
    prev = None
    
    while curr:
        if curr.value == k:
            if curr is l:
                l = curr.next
            else:
                prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
        
    return l



# second solution
# advance the head node until the value isnt k and then check next values
# if next node val is k, remove it from LL, keep curr
# else, advance curr node

def removeKFromList(l, k):
    while l and l.value == k:
        l = l.next
        
    if l == None:
        return l
    
    curr = l
    
    while curr.next:
        if curr.next.value == k:
            curr.next = curr.next.next
        else:
            curr = curr.next
        
        
    return l