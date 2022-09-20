def numDistinct(s,t):
    
    def dfs(s,t):
        if not t:
            return 1
        if len(t) > len(s):
            return 0
        count = 0
        for i in range(len(s)-len(t)+1):
            if t[0] == s[i]:
                count += dfs(s[i+1:],t[1:])
        return count
    return dfs(s,t)

s = 'rabbbit'
t = 'rabbit'
print(numDistinct(s,t))