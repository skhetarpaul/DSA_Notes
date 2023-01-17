class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        if n==0:
            return [newInterval]
        while i<len(intervals) and intervals[i][0]<newInterval[0] and intervals[i][1]<newInterval[0]:
            i+=1
        
        #find if interval is exclusive
        if i<n:
            if i>0 and intervals[i-1][1]<newInterval[0] and intervals[i][0]>newInterval[1]:
                return intervals[:i] + [newInterval] + intervals[i:]
            elif i==0 and intervals[i][0]>newInterval[1]:
                return [newInterval] + intervals[i:]

            else:
                removed = set()
                intervals[i] = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                print(intervals)

                tempi = i+1
                while tempi<n and (intervals[tempi][0]<=intervals[i][1] or intervals[tempi][1]<=intervals[i][1]):
                    if intervals[tempi][0]<=intervals[i][1] and intervals[tempi][1]<=intervals[i][1]:
                        removed.add(tempi)
                        tempi+=1
                        # print(tempi, intervals[tempi][0], intervals[i][1])
                    elif intervals[tempi][0]<=intervals[i][1]:
                        intervals[i][1] = max(intervals[i][1], intervals[tempi][1])
                        removed.add(tempi)
                        tempi+=1
                    else:
                        break
                newintervals = [intervals[i] for i in range(n) if i not in removed]
                return newintervals
        else:
            return intervals + [newInterval]
        #Conflicting case
        


        