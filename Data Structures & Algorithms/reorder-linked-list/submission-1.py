# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # -----------------------------
        # 1️⃣ 找到链表的中点（快慢指针）
        # -----------------------------
        slow = head                # 慢指针，每次走一步
        fast = head.next           # 快指针，每次走两步（从 next 开始可让 slow 落在前半段尾部）

        while fast and fast.next:  # fast 能走两步就继续
            slow = slow.next       # 慢指针走一步
            fast = fast.next.next  # 快指针走两步

        # 循环结束后，slow 指向链表前半段的最后一个节点
        

        # -----------------------------
        # 2️⃣ 反转链表的后半段
        # -----------------------------
        second = slow.next         # 后半段的开头
        slow.next = None           # 将链表从 slow 处断开，分成两段
        prev = None                # 用于反转链表的“前指针”

        while second:              # 标准链表反转模板
            tmp = second.next      # 暂存后继节点
            second.next = prev     # 当前节点指向前一个节点（反转）
            prev = second          # prev 前进
            second = tmp           # second 前进

        # 反转完成后：prev 指向“后半段反转后的头结点”
        

        # -----------------------------
        # 3️⃣ 交替合并前半段（first）与后半段反转后的链表（second）
        # -----------------------------
        first = head              # 前半段起点
        second = prev             # 后半段起点（反转后）

        while second:             # 当后半段还有节点
            temp1 = first.next    # 暂存前半段的下一个位置
            temp2 = second.next   # 暂存后半段的下一个位置

            first.next = second   # 把 second 接到 first 后面
            second.next = temp1   # 再把 second 接回前半段链表的位置

            first = temp1         # 前半段前进
            second = temp2        # 后半段前进

        # 最终链表结构已完成重排（L0 → Ln → L1 → Ln-1 → ...）
