class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r=0,len(numbers)-1
        
        while numbers[l]+numbers[r] != target :
            total=numbers[l]+numbers[r]
            if total > target:
                r-=1
            elif total<target:
                l+=1
        return [l+1,r+1]

        
        

        
        # d = {}
        # for i in range(len(numbers)):
        #     if target - numbers[i] in d:
        #         return [d[target - numbers[i]]+1,i+1]
        #     d[numbers[i]]=i
        