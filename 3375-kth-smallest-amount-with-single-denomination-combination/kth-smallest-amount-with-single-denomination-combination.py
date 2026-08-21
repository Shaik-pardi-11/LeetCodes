import math
from functools import reduce
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins, k):
        def count(x):
            total = 0
            n = len(coins)
            for r in range(1, n+1):
                for comb in combinations(coins, r):
                    lcm = reduce(lambda a,b: a*b // math.gcd(a,b), comb)
                    if r % 2:
                        total += x // lcm
                    else:
                        total -= x // lcm
            return total

        left, right = 1, max(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
