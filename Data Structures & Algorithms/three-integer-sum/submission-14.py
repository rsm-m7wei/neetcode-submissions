class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 目标：找出数组中所有不重复的三元组，使得它们的和为 0。

        # res = []             # 用于保存所有满足条件的三元组
        # nums.sort()          # 排序非常关键（方便去重 + 使用双指针）

        # # 遍历每一个数，把它当作三元组中的“第一个数”
        # for i, n in enumerate(nums):

        #     # 跳过重复的第一个数（防止结果重复）
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue

        #     # 设置左右指针
        #     l = i + 1               # 左指针，指向当前数右边
        #     r = len(nums) - 1       # 右指针，指向数组末尾

        #     # 双指针开始往中间移动
        #     while l < r:
        #         threeSum = nums[i] + nums[l] + nums[r]

        #         if threeSum > 0:     # 和太大 → 右指针左移（减少总和）
        #             r -= 1
        #         elif threeSum < 0:   # 和太小 → 左指针右移（增加总和）
        #             l += 1
        #         else:
        #             # 找到一个合法三元组
        #             res.append([nums[i], nums[l], nums[r]])

        #             # 左指针右移前，先跳过重复的数字（避免重复解）
        #             l += 1
        #             while l < r and nums[l] == nums[l - 1]:
        #                 l += 1
        # return res


        # res = []
        # nums.sort()
        # for i in range(len(nums)-2):
        #     if i>0 and nums[i]== nums[i-1]:
        #         continue
        #     l =i+1
        #     r = len(nums)-1
        #     while l<r:
        #         tsum = nums[i]+nums[l]+nums[r]
        #         if tsum< 0:
        #             l+=1
        #         if tsum>0:
        #             r-=1
        #         if tsum == 0:
        #             res.append([nums[i],nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while l<r and nums[l] == nums[l-1]:
        #                 l+=1
        #             while l<r and nums[r] == nums[r+1]:
        #                 r-=1
        # return res

       

        # res = []
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if i>0 and  nums[i] ==nums[i-1]:
        #         continue
        #     l = i+1
        #     r = len(nums)-1
        #     while l<r:
        #         sumn = nums[i]+nums[l]+nums[r]
        #         if sumn <0:
        #             l+=1
        #         elif sumn >0:
        #             r-=1
        #         else:
        #             res.append([nums[i],nums[l],nums[r]])
        #             l+=1
        #         #当使用while来多步计算的时候都需要机上l <r来确保不会越界
        #             while l<r and nums[l] ==nums[l-1]:
        #                 l+=1
        #             while l < r and r<=len(nums)-2 and nums[r] == nums[r + 1]:
        #                 r -= 1
                
        # return res




        res = []
        nums.sort()
        for i in range(len(nums)-2):
            l =i+1
            r=len(nums)-1
            if nums[i] ==nums[i-1] and i>0:
                continue
            while l<r:
                tsum =nums[i]+nums[l]+nums[r]
                if tsum >0:
                    r-=1
                elif tsum<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return res



                    

                
            


