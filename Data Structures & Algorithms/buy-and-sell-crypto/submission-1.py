class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxProfit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l=r
            r=r+1
        return maxProfit

        # profit=0
        # for i in range(len(prices)):
        #     buy=prices[i]
        #     for j in range(i+1,len(prices)):
        #         sell= prices[j]
        #         if sell-buy > profit:
        #             profit=sell-buy
        # return profit

       
        