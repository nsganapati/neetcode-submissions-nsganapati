class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        sortedNums = sorted(nums)
        count=0
        prevNumber=sortedNums[count]
        for i in range(1,len(sortedNums)):
            if prevNumber == sortedNums[i]:
                return True
            prevNumber=sortedNums[i]
            count=count+1
        return False