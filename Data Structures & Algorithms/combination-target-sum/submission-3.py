class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        # #如果我需要把“当前状态”存下来，并且这个状态之后还会被修改——就必须 copy。

        # res= [] # 顶出两个我们要用的东西，一个是我们希望sort一遍列表，还需要一个空的list来接住回答
        # def comb(curr,start,target): # dfs， 首先定义退出，也就是最后true的条件，这里是target = 0 也就是等于他
        #     if target == 0:
        #         res.append(curr)
        #         return # 跳出这个一整个组合
        #     for i in range(start, len(nums)):
        #         if nums[i]>target:
        #             break #和return 不一样，这里仅仅是不运行下面的这一行
        #         comb(curr+[nums[i]],i,target-nums[i]) # 注意这里是两层括号
        #     return
        # comb([],0,target) # 初始条件，我们需要什么，一个空的list每次递归都用，一个指针到0，一个target作为我们的目标
        # return res

        # #创建一个list来存放回答
        # res =[]
        # #创建一个函数来做dfs,需要指针i确定是不是要用当前的数字，用curr(list)来记录我们现在用了哪些数字，以及sums来记录当前的数字合
        # def dfs(i,curr,sums):
        #     #不需要递归的基本情况：没有，或者符合要求
        #     if sums ==target:
        #         #!!因为 curr 在回溯过程中会被反复修改，不 copy() 的话，存进 res 的结果会被后续修改污染。
        #         res.append(curr.copy())
        #         return 
        #     if i>= len(nums) or sums>target:
        #         return
        #     #接下来分两种情况来递归，一个是我们要用当前i指向的数字
        #     curr.append(nums[i])
        #     dfs(i,curr,sums+nums[i])
        #     #或者不用当前的数字，我们把他pop出来之后移动指针，限制只能用后面的数字
        #     curr.pop()
        #     dfs(i+1,curr,sums)
        # #初始化调用递归函数
        # dfs(0,[],0)
        # return res


        #used to store ressult
        res=[]
        #we can use number in and after index i,curr means list of number we are considering,sums means total sum so far
        def dfs(i,curr,sums):
            #baseic case
            if sums ==target:
                res.append(curr.copy())
                return
            #case when we need to stop
            if i>=len(nums) or sums>target:
                return
            #two cases if we want to sue current number
            #case: using current number
            curr.append(nums[i])
            dfs(i,curr,sums+nums[i])
            #case: not using current number
            #pop out number we just added
            curr.pop()
            dfs(i+1,curr,sums)
        #initial fuction
        dfs(0,[],0)
        return res


                


    # def combinationSum2(nums, target):
    #     nums.sort()  # ✅ 1) 先排序，方便去重/剪枝

    #     res = []

    #     def dfs(i, curr, sums):
    #         if sums == target:
    #             res.append(curr.copy())
    #             return
    #         if i >= len(nums) or sums > target:
    #             return

    #         # ✅ 2) 选 nums[i]：由于每个元素只能用一次，所以递归用 i+1
    #         curr.append(nums[i])
    #         dfs(i + 1, curr, sums + nums[i])   # ✅ 从 dfs(i, ...) 改成 dfs(i+1, ...)
    #         curr.pop()

    #         # ✅ 3) 不选 nums[i]：跳过所有和 nums[i] 相同的元素，避免重复组合
    #         j = i
    #         while j + 1 < len(nums) and nums[j + 1] == nums[i]:
    #             j += 1
    #         dfs(j + 1, curr, sums)             # ✅ 从 dfs(i+1, ...) 改成 dfs(j+1, ...)

    #     dfs(0, [], 0)
    #     return res


            



        
            