#User function Template for python3

#Note the pattern, something relates to something and order needs to be found out. Topo sort can be applied.
#SOMETHING BEFORE SOMETHING
from queue import Queue

class Solution:
    def findOrder(self,dict, N, K):
    # code here
        adj = [[] for i in range(K)]
        l = len(dict)
        indeg = [0 for i in range(K)]
        def findDifferentItems(s1, s2):
            l = min(len(s1), len(s2))
            for i in range(l):
                if s1[i]==s2[i]:
                    continue
                elif s1[i]!=s2[i]:
                    return [ord(s1[i])-97, ord(s2[i])-97]
            # print("here")
            return [None, None]
                
        
        for i in range(0, len(dict)-1):
            # print(dict[i], dict[i+1])
            na,nb = findDifferentItems(dict[i], dict[i+1])
            if na is None and nb is None:
                continue
            adj[na].append(nb)
            indeg[nb]+=1
        q = Queue()
        ans = []
        for i in range(K):
            if indeg[i]==0:
                q.put(i)
        while not q.empty():
            temp = q.get()
            for nbr in adj[temp]:
                indeg[nbr]-=1
                if indeg[nbr]==0:
                    q.put(nbr)
            ans.append(temp)
        s = ""
        for i in ans:
            s+=chr(i + 97)
        return s
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends