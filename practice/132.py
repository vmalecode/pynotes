from sortedcontainers import SortedList
def minCut(s):
    res = []
    r = SortedList()
    def dfs(s,path):
        if not s:
            res.append(path)
            return
        for i in range(1,len(s)+1):
            if checkPal(s[:i]):
                dfs(s[i:],path+[s[:i]])
    dfs(s,[])
    print(res)
    
    
def checkPal(s):
    if len(s) <= 1:
        return True
    l,r = 0,len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
s = 'aab'
print(minCut(s))