class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1]*(len(nums)) #1 初始化一个和list长度相等的list，后面的len外面的（）其实是可以省略的，但是为了表示清楚计算顺序还是需要写上去了
        # prefix =1 # 因为是乘法所以初始化时是1
        # for i in range(len(nums)): #2 首先的任务是在对应的位置存入prefix，之后计算出对应的posfix再相乘法
        #     res[i]= prefix # 为了实现错位，先存入prefix到对应的位置之后再更新prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums)-1,-1,-1):
        # ！！range是包含起点，不包含终点，所以这里才需要len()-1，来包含起点，而我们需要也包含终点，所以这里写-1
        #     res[i]*= postfix # 先和prefix乘法再更新postfix
        #     postfix *= nums[i]
        # return res
    
        #计算出每一个位置的前序的乘将，再和对应位置的后序乘就行

        #建立一个和数字一样长的list全放1
        res =[1]*len(nums)
        #初始化前缀和
        prefix =1
        for i in range(len(nums)):
            #因为要错位，所以我们先存再更新prefix
            res[i] = prefix
            prefix *= nums[i]
        postfix =1
        for i in range(len(nums)-1,-1,-1):
            res[i] *=postfix
            postfix *= nums[i]
        return res


        # res =[1]*len(nums)
        # prefix =1
        # for i in range(len(nums)):
        #     res[i] =prefix
        #     prefix *= nums[i]
        # postfix =1
        # for j in range(len(nums)-1,-1,-1):
        #     res[j] *= postfix
        #     postfix *=nums[j]
        # return res
       
            
        