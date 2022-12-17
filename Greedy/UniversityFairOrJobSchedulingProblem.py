from functools import cache
from typing import List
#This is a Greedy Problem following Pattern for Job schedulng Algorithm.

def max_presentations(starts: List[int], durations: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(starts)
#     end = [duration[i] + starts[i] for i in range(n)]
    combined = sorted(zip(starts, durations), key = lambda x: (x[0]+x[1],x[1]))
    #greedy approach
    count = 1
    currend = combined[0][0] + combined[0][1]
    for i in range(1,n):
        if combined[i][0]>=currend:
            currend = combined[i][0] + combined[i][1]
            count+=1
    return count
# @cache
def max_presentations(starts: List[int], durations: List[int]) -> int:
    n = len(starts)
    combined = sorted(zip(starts, durations), key = lambda x: (x[0]+x[1],x[1]))
    def recursion(index, finish):
        if index==n:
            return 0
        elif combined[index][0]<finish:
            return recursion(index+1, finish)
        else:
            notpick = recursion(index+1, finish)
            pick = 1 + recursion(index+1, combined[index][0] + combined[index][0])
            return max(pick, notpick)
    

if __name__ == '__main__':
    starts = [int(x) for x in input().split()]
    durations = [int(x) for x in input().split()]
    res = max_presentations(starts, durations)
    print(res)
