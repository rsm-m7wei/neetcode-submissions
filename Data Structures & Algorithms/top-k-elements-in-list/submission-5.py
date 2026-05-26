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
        #用字典计数，
        #创建列表套列表（桶），按照出现的频率把对应的字符放进去，并且从最后开始倒着遍历，直到找到对应的数量
        freq = [[] for i in range(len(nums)+1)]
        #

        for num in nums:
            count[num]=count.get(num,0)+1
        
        for ind, val in count.items():
            #这里val是出现的次数，ind才是数字
            freq[val].append(ind)

        res=[]
        for i in range(len(freq)-1,0,-1):
            #从最后倒折一个个的取出list，并且把每个list里面的元素取出来放到res中，当res长度满足要求就返回
            for n in freq[i]:
                res.append(n)
                if len(res) ==k:
                    return res

    #建立dict来拖你关机频次
    #建立bucket把frequent对应的方进去
    #建立res ，从末尾遍历bucket来取出对应的格子，再把格子里面的数字取出来加入res

        count ={}
        freq =[[]for i in range(len(nums)+1)]
        for i in nums:
            count[i] =count.get(i,0)+1

        for ind, val in count.items():
            freq[val].append(ind)
        
        res =[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) ==k:
                    return res
    



        


        

