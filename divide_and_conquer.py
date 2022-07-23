class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.findMaximumSubarray(nums, 0, len(nums)-1)
    
    def findMaximumSubarray(self, nums, l, r):
        # empty array
        if l > r:
            return -math.inf
        
        mid = (l + r) // 2 
        curr = lsum = rsum = 0
        
        for i in range(mid - 1, l - 1, -1):
            curr += nums[i]
            lsum = max(lsum, curr)
            
        curr = 0
        for i in range(mid + 1, r + 1):
            curr += nums[i]
            rsum = max(rsum, curr)            
        
        # ここで左右どっちも-で、midもマイナスだとしても、-値のマックス値が生まれる可能性がある(0マックスにならない)
        mixsum = nums[mid] + lsum + rsum
        
        lremain = self.findMaximumSubarray(nums, l, mid - 1)
        rremain = self.findMaximumSubarray(nums, mid + 1, r)
        
        return max(mixsum, lremain, rremain)
