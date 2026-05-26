class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 🧩 1️⃣ 初始化左右指针
        # ⚠️ 注意写法要是 l, r = 0, len(nums) - 1，不能写 l = 0, 否则 l 变成元组 (0,)
        # l, r = 0, len(nums) - 1

        # # 🧩 2️⃣ 记录当前找到的最小值
        # # 先设为 nums[0]，后面用 min() 不断更新
        # res = nums[0]

        # # 🧩 3️⃣ 进入二分循环
        # while l <= r 的意思是：
        # “只要搜索区间 [l, r] 还没排除完，就继续找”
        # 这是所有二分查找的模板条件。
        # while l <= r:
        #     # ✅ 如果当前区间已经是升序的，说明最小值一定在 nums[l]
        #     # 直接更新并用 break 提前退出（不用再二分）
        #     if nums[l] <= nums[r]:
        #         res = min(res, nums[l])
        #         break

        #     # 🧩 4️⃣ 计算中点
        #     m = (l + r) // 2

        #     # ✅ 每次遇到一个候选值，都更新一下最小值
        #     # 因为我们不知道最小值在左边还是右边
        #     res = min(res, nums[m])

        #     # 🧩 5️⃣ 判断最小值在哪一半：
        #     # 如果左半边 [l..m] 是有序的，最小值不可能在这里（因为升序部分的最小值在最左边）
        #     if nums[m] >= nums[l]:
        #         # 所以把搜索范围移到右边
        #         l = m + 1
        #     else:
        #         # 否则右半边是有序的，最小值一定在左边
        #         r = m - 1

        # # 🧩 6️⃣ 返回结果
        # return res

        #初始化两个指针，以及一个放回答的
        l= 0
        r =len(nums)-1
        res =nums[0]
        while l<= r:
            if nums[l]<=nums[r]:
                res=min(res,nums[l])
                break
            m =(l+r)//2
            res =min(res,nums[m])
            if nums[m]>=nums[l]:
                l=m +1
            else:
                r = m-1
        return res

        #初始化两个指针指向左右
        #初始化res
        l =0
        r =len(nums)-1
        #随便初始化一个数字
        res = nums[0]
        while l<r:
            if nums[l]<nums[r]:
                res =min(nums[l],res)
                #如果已经找到了就得break跳过下面的操作
                break
            m = (l+r)//2
            #为了防止中间点是最小点，我们需要先比较中间点
            res =min(res,nums[m])
            if nums[m]>nums[l]:
                l = m+1
            else:
                r =m-1
        return res
            

