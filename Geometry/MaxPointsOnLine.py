#Simple geometry question utilizing O(n2) methodology.
#This uses a dictionary of dictionary.


class Solution:
    def maxPoints(self, points):
        if len(points) in [1,2]:
            return len(points)
        d = {}
        maxi = 2
        for i in range(len(points)):
            px, py = points[i]
            d[(px, py)] = {}
            d[(px, py)][float("inf")] = 1
            for j in range(len(points)):
                if j!=i:
                    jx, jy= points[j]
                    if (jx-px)!=0:
                        if (jy-py)/(jx-px) in d[(px, py)]:
                            d[(px, py)][(jy-py)/(jx-px)]+=1
                            maxi = max(maxi, d[(px, py)][(jy-py)/(jx-px)])
                        else:
                            d[(px, py)][(jy-py)/(jx-px)] = 2
                    else:
                        d[(px, py)][float("inf")]+=1
                        maxi = max(maxi, d[(px, py)][float("inf")])
        print(d.items())
        return maxi
                        