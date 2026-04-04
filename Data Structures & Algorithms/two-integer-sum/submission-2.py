class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3, 4, 5, 6 #target = 10
        for i in range(0,len(nums)): #3
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
            

        