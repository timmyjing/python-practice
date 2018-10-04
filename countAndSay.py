# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
#         recursive, take the previous solution and count the ones and twos
        if n == 1:
            return str(n)
        
        prev = self.countAndSay(n - 1)
        
        result = ""
        curr = None
        count = 0
        
        for i in str(prev):
            if curr == None:
                curr = i
                count = 1
            elif curr != i:
                result += str(count) + str(curr)
                curr = i
                count = 1
            else:
                count += 1
                
        if count >= 1:
            result += str(count) + str(curr)
        
        return result
            
        