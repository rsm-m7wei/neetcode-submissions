# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 如果列表为空或不存在链表，直接返回 None
        if len(lists) == 0 or not lists:
            return None
        
        # 不断进行 pairwise 合并，直到只剩一个链表
        while len(lists) > 1:
            mergedlists = []   # 用来存放每一轮合并后的链表

            # 每次取两个链表进行合并（步长为 2）
            for i in range(0, len(lists), 2):
                l1 = lists[i]                         # 当前链表
                l2 = lists[i+1] if i+1 < len(lists) else None   # 下一个链表（可能不存在）
                
                # 将 l1 和 l2 合并后放入 mergedlists
                mergedlists.append(self.mergelist(l1, l2))
            
            # 更新 lists，继续下一轮合并
            lists = mergedlists
        
        # 当 lists 长度为 1 时，lists[0] 就是最终合并后的链表头
        return lists[0]

    def mergelist(self, l1, l2):
        # 使用 dummy 节点简化链表操作
        dummy = ListNode()
        tail = dummy

        # 当两个链表都不为空时，逐节点比较并接到 tail 后面
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1     # 选更小的节点
                l1 = l1.next       # l1 前进
            else:
                tail.next = l2     # 选更小的节点
                l2 = l2.next       # l2 前进
            tail = tail.next       # tail 前进

        # 如果 l1 或 l2 还有剩余，直接拼接到 tail 后面
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # 返回合并后链表的头（dummy.next）
        return dummy.next
