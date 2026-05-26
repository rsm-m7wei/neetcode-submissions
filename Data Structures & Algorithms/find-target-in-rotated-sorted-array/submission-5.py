class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l = 0
        # r =len(nums)-1
        # while l<=r:
        #     m = (l+r)//2
        #     if target == nums[m]:
        #         return m
        #     if nums[l]<=nums[m]:
        #         if target<nums[l] or target>nums[m]:
        #             l =m+1
        #         else:
        #             r= m-1
        #     else:
        #         if target>nums[r] or target<nums[m]:
        #             r =m-1
        #         else:
        #             l =m+1
        # return -1

        l =0
        r= len(nums)-1
        while l<=r:
            #一定是要<=,避免中间有丢失的情况
            m =(l+r)//2
            if target == nums[m]:
                return m
                #左半边是有序的，中点之后还有有序部分
            if nums[l]<= nums[m]:
                if target<nums[l] or target>nums[m]:
                    l=m+1
                else:
                    r =m-1
            #右边是有序的，且中点左边还有有序部分
            else:
                if target>nums[r] or target<nums[m]:
                    #往左找
                    r =m-1
                    #往右找
                else:
                    l=m+1
        #都没找到的话就返回-1           
        return -1
