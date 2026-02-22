class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        
       
        positions = [i for i, bit in enumerate(binary) if bit == '1']
        
        
        if len(positions) < 2:
            return 0
        
        
        max_gap = max(positions[i+1] - positions[i] for i in range(len(positions)-1))
        
        return max_gap

        