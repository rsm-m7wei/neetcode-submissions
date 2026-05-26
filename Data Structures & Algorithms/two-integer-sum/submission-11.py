class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # premap= {} # 因为我们关心位置，所以我们需要创造一个字典
        # for i, num in enumerate(nums): # 这里是想要把 nums 里面的组合取出来，注意enumerate怎么写
        #     diff = target - num # 求出diff是多少
        #     if diff in premap: # 这里情况二： 看看diff在不在premap的key里面
        #         return [premap[diff],i] # 在的话就可以return了
        #     premap[num] = i # 情况一： 如果没有的话就把num存进去，以后好找diff,！！注意这里是数字作为key，编号作为value，因为我要搜索数字。是不是可以理解为最后要的作为value呢？
        # return False

        #维护一个字典，把原来数列里面的数值和位置存进去，每次遍历都查找
        
        # sums ={}
        # for ind, num in enumerate(nums):
        #     diff = target - num
        #     if diff in sums:
        #         return [sums[diff],ind]
        #     sums[num] = ind
        # return False

        # #哈希字典
        # sums= {}
        # for ind, nums in enumerate(nums):
        #     dif = target -nums
        #     if dif in sums:
        #         return [sums[dif],ind]
        #     #如果不在的话就加入字典
        #     sums[nums] =ind
        # #遍历完成之后还是没有的话就return false
        # return False


        # dic ={}
        # for ind, num in enumerate in nums:
        #     dif = target -num
        #     if dif in dic:
        #         return [dic[dif],ind]
        #     dic[num] =ind
        # return False

        #创建一个字典来储存
        seen ={}
        for ind, num in enumerate(nums):
            #对每一个数值我们都要检查是不是有满足条件的diff，有的话就返回，没有的话就把目前的加入
            #注意我们是通过num找indx
            diff  = target -num
            if diff in seen:
                return [seen[diff],ind]
            seen[num] =ind
        return False





