def subsetsWithDup(nums):
      res = []
      def dfs(path,idx):
          res.append(path)
          for i in range(idx,len(nums)):
              if i > idx and nums[i-1] == nums[i]:
                  continue
              dfs(path+[nums[i]],idx+1)
      dfs([],0)
      return res
n = [1,2,2]
print(subsetsWithDup(n))