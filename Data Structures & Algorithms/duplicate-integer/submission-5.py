class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:  # 不用关心self，只需要看后面输入和输出的预期类型就行
        # seen= set() # 创造一个空hashset，选set是因为他是无重复的，不选dic是应为我们不关心num 它出现了几次、在哪出现
        # for num in nums: # 对于给定的列表里面的每一个元素, 并且这里面有
        #     if num in seen:
        #         return True # 这里有了return,break, continue 之后就不用写 else，他不会跑同样缩进级别的代码
        #     seen.add(num) 
        # return False


        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False
    
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            elif i in seen:
                return True
        return False
