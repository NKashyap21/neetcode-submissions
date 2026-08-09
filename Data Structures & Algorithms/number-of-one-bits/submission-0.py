class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)[2:]
        count = 0
        for num in bin_n:
            if num == "1": count += 1
        return count