class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        cnt=0
        prod=1

        for num in nums:   
            if num !=0:
                prod=prod*num
            else:
                cnt+=1
            if cnt > 1:
                return [0]*len(nums)

        if cnt:
            for num in nums:
                if num !=0:
                    result.append(0)
                else:
                    result.append(prod)
            return result
        
        for num in nums:
            res=prod/num
            result.append(int(res))
        return result


        # Solution 1
        # result=[]

        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             prod = prod * nums[j]
        #     result.append(prod)
        # return result
        