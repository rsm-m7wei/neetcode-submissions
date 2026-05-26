# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ---------------------------------------
        # 1️⃣ 用快慢指针找到链表中点（slow 停在前半段的最后一个节点）
        # ---------------------------------------
        slow = head
        fast = head.next     # fast 从 next 开始，有助于让 slow 落在前半段尾部

        while fast and fast.next:   # fast 每次走两步
            slow = slow.next        # slow 每次走一步
            fast = fast.next.next

        # slow 停的位置是前半段的尾部
        second = slow.next          # second 指向后半段开头
        slow.next = None            # ⚠️ 断开前后两段链表


        # ---------------------------------------
        # 2️⃣ 反转后半段链表
        # ---------------------------------------
        pre = None
        curr = second

        # 标准链表反转模板：curr → pre
        while curr:
            tmp = curr.next     # 暂存后一个节点
            curr.next = pre     # 当前节点指向前一个节点（反转）
            pre = curr          # pre 前进
            curr = tmp          # curr 前进
        
        # 反转完成后：pre 指向“后半段反转后的头结点”


        # ---------------------------------------
        # 3️⃣ 合并链表：前半段(first) 和 反转后的后半段(second)
        #    交替连接，形成 L0 → Ln → L1 → Ln-1 → ...
        # ---------------------------------------
        first = head            # 前半段起点
        second = pre            # 后半段（已反转）起点

        # 当 second 还有节点时（front 的节点可能更多，但不用管）
        while second:
            temp1 = first.next  # 前半段下一节点暂存
            temp2 = second.next # 后半段下一节点暂存

            first.next = second # 前半段当前节点连到后半段当前节点
            second.next = temp1 # 后半段当前节点连回前半段下一节点

            first = temp1       # 前半段往前推进
            second = temp2      # 后半段往前推进

        # 所有操作完成，链表已按题意完成重排
