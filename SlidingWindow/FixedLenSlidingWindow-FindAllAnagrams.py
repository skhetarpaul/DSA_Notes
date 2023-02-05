# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

'''This is a straigit question of Fixed length sliding window where we need to compute the matching set of characters i.e. Anagrams.

Note that, word Anagram might suggest the use of dictionaries as anagrams are same letters in a different sequence though letters always remain the same.'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        pdict = {}
        for i in p:
            if i in pdict:
                pdict[i]+=1
            else:
                pdict[i] = 1
        sdict = {}
        if len(s)<len(p):
            return []
        i,j = 0,0
        while j<len(s):
            
            #Adding to dictionary
            if s[j] in sdict:
                sdict[s[j]]+=1
            else:
                sdict[s[j]] = 1
            print(sdict, i, j, j-i+1)
            if j-i+1<len(p):
                j+=1
            #equivalence case
            elif j-i+1==len(p):
                #check for equivalence
                if sdict==pdict:
                    res.append(i)
                sdict[s[i]]-=1
                if sdict[s[i]]==0:
                    sdict.pop(s[i])
                i+=1
                j+=1
        return res

