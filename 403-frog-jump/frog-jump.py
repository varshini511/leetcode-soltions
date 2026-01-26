class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        stone_set = set(stones)
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for k in dp[stone]:
                for step in (k - 1, k, k + 1):
                    if step > 0 and stone + step in stone_set:
                        dp[stone + step].add(step)

        return len(dp[stones[-1]]) > 0
