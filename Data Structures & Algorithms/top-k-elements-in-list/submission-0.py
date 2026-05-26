class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[]for i in range(len(nums)+1)]
        for n in nums:
            count[n]= count.get(n,0)+1 # 通过前面建立的dict记数，此时数字作为key，频率作为value
        for n, c in count.items(): 
            freq[c].append(n) #是用频率作为key，里面的数字作为value来简历桶

        res =[]
        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]: #这里是从桶里面取出top的内容
                res.append(n)
                if len(res) == k:
                    return res