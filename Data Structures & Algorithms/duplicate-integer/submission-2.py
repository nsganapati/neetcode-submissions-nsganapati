from collections import defaultdict
from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

        
        
        # numbDict=Counter(nums)
        
        # numDict=defaultdict(int)
        # print(f"Before : {numDict}")
        # for i in nums:
        #     numDict[i]=numDict[i]+1
        # print(f"After : {numDict}")
        # for i in numDict.values():
        #     if i>1:
        #         return True
        # return False



        # Solution 1
        # sortedNums = sorted(nums)
        # count=0
        # prevNumber=sortedNums[count]
        # for i in range(1,len(sortedNums)):
        #     print(prevNumber)
        #     print(sortedNums[i])
        #     if prevNumber == sortedNums[i]:
        #         return True
        #     prevNumber=sortedNums[i]
        #     count=count+1
        # return False

        #Solution 1
        # if not nums:
        #     return False
        # sortedNums = sorted(nums)
        # count=0
        # prevNumber=sortedNums[count]
        # for i in range(1,len(sortedNums)):
        #     if prevNumber == sortedNums[i]:
        #         return True
        #     prevNumber=sortedNums[i]
        #     count=count+1
        # return False