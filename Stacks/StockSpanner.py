# A variation of Next Greater element to the right
# https://leetcode.com/problems/online-stock-span/submissions/
class StockSpanner:

    def __init__(self):
        self.stk = []
        self.index = 0


    def next(self, price: int) -> int:
        print("price", price)
        while not len(self.stk)==0 and self.stk[-1][0]<=price:
            self.stk.pop()
        if len(self.stk)==0:
            self.stk.append((price, self.index))
            ans = self.index+1
            self.index+=1
            return ans
        else:
            previndex = self.stk[-1][1]
            # print(previndex, "previondex")
            self.stk.append((price, self.index))
            # print(self.stk)
            ans = self.index-previndex
            self.index+=1
            return ans
    

    


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)