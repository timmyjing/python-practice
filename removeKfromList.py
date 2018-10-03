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