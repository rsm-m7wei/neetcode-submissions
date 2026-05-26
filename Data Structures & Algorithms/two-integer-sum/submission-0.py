class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap= {} # 因为我们关心位置，所以我们需要创造一个字典
        for i, num in enumerate(nums): # 这里是想要把 nums 里面的组合取出来，注意enumerate怎么写
            diff = target - num # 求出diff是多少
            if diff in premap: # 这里情况二： 看看diff在不在premap的key里面
                return [premap[diff],i] # 在的话就可以return了
            premap[num] = i # 情况一： 如果没有的话就把num存进去，以后好找diff,！！注意这里是数字作为key，编号作为value，因为我要搜索数字。是不是可以理解为最后要的作为value呢？
        return False





