class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


sol = Solution()
nums1 = [1,2,3]
sol.nextPermutation(nums1)
print(nums1)  

nums2 = [3,2,1]
sol.nextPermutation(nums2)
print(nums2) 

nums3 = [1,1,5]
sol.nextPermutation(nums3)
print(nums3)  