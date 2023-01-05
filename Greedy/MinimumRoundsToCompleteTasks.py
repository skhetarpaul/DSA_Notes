from collections import defaultdict

class Solution:
    def minimumRounds(self, tasks):
        counter = defaultdict(int)
        for t in tasks:
            counter[t]+=1
        ans = 0
        for key, val in counter.items():
            print(key, val)
            if val==1:
                return -1
            elif val%3==0:
                print("case div by 3", val//3, ans)
                ans+=val//3
            else:
                
                totalsum = key*val
                print("totalsum initially", val)
                while val>0 and val%3!=0:
                    val-=2
                    ans+=1
                    print("totalsum now", val)
                ans+=val//3
                

                print("case not div by 3", ans)
        return ans
        