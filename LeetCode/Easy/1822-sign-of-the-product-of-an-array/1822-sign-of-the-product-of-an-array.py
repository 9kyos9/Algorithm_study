class Solution(object):
    def arraySign(self, nums):
        res = 1
        for i in range(len(nums)):
            if nums[i] == 0 :
                return  0
            elif nums[i] < 0 :
                res *= -1
        return res
        