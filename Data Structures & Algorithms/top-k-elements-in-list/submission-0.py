from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency map creation
        f=Counter(nums)
        #{1:1,2:2,3:3}
        arr=[]
        for item,value in f.items():
            arr.append([value,item])
        arr.sort(reverse=True)
        #1st frequency, 2nd is integer
        [[3,3],[2,2],[1,1]]
        result=[]
        for i in range(k):
            result.append(arr[i][1])
        return result


        