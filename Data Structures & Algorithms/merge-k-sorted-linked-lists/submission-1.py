# LeetCode 自带的单链表定义（题目里已经给出）
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional   # 记得在本地跑要加这一行类型提示的导入

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        把 k 个有序链表合并成 1 个有序链表。
        思路：利用“分治 / 两两合并”的方式，每一轮把链表成对合并，
        把 k 个链表变成 k/2 个，反复直到只剩一个。
        
        时间复杂度：O(N log k)，N 是所有节点总数，k 是链表个数。
        """

        # ❗ 边界情况 1：lists 本身是 None 或空列表 []
        # not lists 处理 None 或 []
        # len(lists) == 0 其实在 not lists 为 True 时已经覆盖了，这里写不写都行
        if not lists or len(lists) == 0:
            return None
        
        # 当还剩不止一个链表时，就继续两两合并
        while len(lists) > 1:
            mergedlist = []   # 存这一轮两两合并后的新链表们

            # 步长为 2：每次取 (i, i+1) 两个链表合并
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # 可能链表个数是奇数，最后一个没有配对，就让 l2 = None
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                # 把 l1 和 l2 合并，得到新的有序链表头结点
                mergedlist.append(self.mergelist(l1, l2))

            # 用这一轮合并后的结果，作为下一轮需要继续合并的链表数组
            lists = mergedlist

        # 最后只剩下一个链表，就是答案
        return lists[0]
    
    def mergelist(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        合并两个有序链表（LeetCode 21 题同款）
        返回合并后的有序链表的头结点。
        """

        # dummy 是“假头结点”，方便统一处理头结点，无需单独判断第一次插入
        dummy = ListNode()
        tail = dummy  # tail 指针永远指向当前合并链表的最后一个节点

        # 当 l1 和 l2 都还没走到头时，循环比较二者当前节点
        while l1 and l2:
            if l1.val < l2.val:
                # l1 当前节点值更小，把 l1 接到 tail 后面
                tail.next = l1
                # l1 往后走
                l1 = l1.next
            else:
                # l2 当前节点值更小或相等，把 l2 接到 tail 后面
                tail.next = l2
                # l2 往后走
                l2 = l2.next

            # tail 也要往后移动到新加的节点
            tail = tail.next

        # 跳出 while 说明至少有一个链表已经走到头
        # 剩下的那个链表本身就是有序的，直接整体挂后面即可
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # 返回真正的头结点：dummy.next（dummy 自己是个占位节点）
        return dummy.next
