class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)   # XOR with shifted version
        return (x & (x + 1)) == 0

        