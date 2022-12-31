#An important question utilizing importance of Priority Queues.
# https://leetcode.com/problems/single-threaded-cpu/description/
import heapq
class Solution:

    def getOrder(self, tasks):
        combined = [[i[0], i[1]] for i in sorted(enumerate(tasks), key = lambda x: (x[1][0], x[1][1]))]
        ans = [combined[0][0]]
        endTime = combined[0][1][0]+combined[0][1][1]
        index = 1
        hq = []
        while index<len(combined):
            if combined[index][1][0]<=endTime:
                heapq.heappush(hq, [combined[index][1][1], combined[index][0],combined[index][1][0]])
                index+=1
            elif len(hq)==0:
                ans.append(combined[index][0])
                endTime =  combined[index][1][0]+combined[index][1][1]
                
                index+=1
            else:
                #enditme needs to be increased
                processing,i, start = heapq.heappop(hq)
                endTime = endTime+processing
                ans.append(i)
        while len(hq)>0:
            processing,i, start = heapq.heappop(hq)
            ans.append(i)
        print(combined)
        # return [1,2]
        return ans