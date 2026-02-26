class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
    
    # Traverse from right to left (excluding the most significant bit)
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:  # odd
                steps += 2   # one for +1, one for /2
                carry = 1    # propagate carry
            else:            # even
                steps += 1   # just divide by 2
    
    # Finally, if there's a carry left at the most significant bit
        return steps + carry

        