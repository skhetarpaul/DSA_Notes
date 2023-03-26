'''Notice the use of method like splitlines-> splits into array separated by line or \n.
lstrip -> strips off the required characters provided as arg in lstrip
https://leetcode.com/problems/longest-absolute-file-path/description/
NEW_PROBLEMLIST_PAGE=1; '''


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line)-len(name)

            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen
        
