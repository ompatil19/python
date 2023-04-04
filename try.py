class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        while(1):
            mi=min(prices)
            mi_ind=prices.index(mi)
            b=prices[mi_ind::]
            if(b):
                ma=max(b)
                return b-mi
            else:
                prices.remove(mi)
            # print("max",ma)
            # print("min",mi)
            # if(prices.index(ma)>=prices.index(mi)):
            #     # print(prices.index(ma))
            #     # print(prices.index(mi))
            #     return ma-mi
            #     break
            # else:
            #     if prices.index(ma)<prices.index(mi):
            #         prices.remove(ma)
            #     else:
            #         prices.remove(mi)
# a=[1]
# print(max(a))