class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}  # 计数器
        # freq = [[] for i in range(len(nums) + 1)]  # 桶，索引=出现次数

        # # 1️⃣ 统计出现频率
        # for x in nums:
        #     count[x] = count.get(x, 0) + 1

        # # 2️⃣ 把数字放进对应的频率桶里
        # for n, c in count.items():
        #     freq[c].append(n)

        # # 3️⃣ 从高频到低频取出前 k 个
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        count ={}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num]=count.get(num,0)+1
        
        for ind, val in count.items():
            freq[val].append(ind)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) ==k:
                    return res


        

