class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res= [] # 顶出两个我们要用的东西，一个是我们希望sort一遍列表，还需要一个空的list来接住回答
        def comb(curr,start,target): # dfs， 首先定义退出，也就是最后true的条件，这里是target = 0 也就是等于他
            if target == 0:
                res.append(curr)
                return # 跳出这个一整个组合
            for i in range(start, len(nums)):
                if nums[i]>target:
                    break #和return 不一样，这里仅仅是不运行下面的这一行
                comb(curr+[nums[i]],i,target-nums[i]) # 注意这里是两层括号
            return
        comb([],0,target) # 初始条件，我们需要什么，一个空的list每次递归都用，一个指针到0，一个target作为我们的目标
        return res


        nums.sort()
        res= []
        def comb(start, curr, target):
            if target ==0:
                res.append(curr)
            for i in range(start, len(nums)):
                if nums[i]>target:
                    break
                comb(i,curr+[nums[i]],target-nums[i])
            return
        comb(0,[],target)
        return res

        nums.sort()
        res=[]
        def comb(start,curr, target):
            if target == 0:
                res.append(curr)
            for i in range(nums):
                if nums[i]>target:
                    break
                comb(i,[curr+nums[i]], target-nums[i])
            return
        comb(0,[],target)
        return res


