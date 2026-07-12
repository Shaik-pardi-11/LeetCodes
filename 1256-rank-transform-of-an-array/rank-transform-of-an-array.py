class Solution:
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(set(arr))
        rank_map = {num: i+1 for i, num in enumerate(sorted_unique)}
        return [rank_map[num] for num in arr]


# Example usage
sol = Solution()
print(sol.arrayRankTransform([40,10,20,30]))   # [4,1,2,3]
print(sol.arrayRankTransform([100,100,100]))   # [1,1,1]
print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12]))  # [5,3,4,2,8,6,7,1,3]
