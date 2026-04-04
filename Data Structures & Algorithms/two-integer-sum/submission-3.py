class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            value = target - nums[i]
            if value in d:
                return [d[value],i]
            d[nums[i]]=i
            print(d)
         

        # for i in range(0,len(nums)): #3
        # #     for j in range(i+1,len(nums)):
        # #         if nums[i]+nums[j] == target:
        # #             return [i,j]

        # for i in range(0,len(nums)): #3
        #     for j in range(1,len(nums)):
        #         if i==j:
        #            continue
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
            

        