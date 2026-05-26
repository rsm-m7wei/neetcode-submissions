# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pre 指向“已反转部分”的表头；一开始还没有反转任何节点，所以是 None
        pre = None
        # curr 是工作指针，从当前还未反转的链表头开始走
        curr = head

        # ⚠️ 易错点：一定是 while curr（谁在变就看谁），不要写 while head
        while curr:
            # 1) 先保存下一节点。⚠️ 不提前保存会在下一步断链后丢失后半段
            nxt = curr.next

            # 2) 核心反转：把当前节点的 next 指向“前一个”（也就是已反转部分的表头 pre）
            curr.next = pre

            # 3) 两个指针整体右移：pre 前进一步成为新的表头；curr 继续处理下一节点
            pre = curr
            curr = nxt

        # 循环结束时：
        # - curr == None（已经走到尾部之后）
        # - pre 指向“反转后链表”的新表头
        # ⚠️ 易错点：必须 return pre，而不是 return head（head 仍指向旧的第一个节点，此时已变成尾巴）
        return pre

        
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1) 递归终止条件（base case）：
        #    链表为空时，直接返回 None，防止继续访问 head.next 报错
        if not head:
            return None

        # 2) 默认把 newHead 设为 head：
        #    这是“兜底”做法：当只有一个节点时不会进入递归分支，直接返回自己作为新表头
        newHead = head

        # 3) 如果后面还有节点，先把“后半段”全反过来（分而治之）
        if head.next:
            # 3.1 递归处理 head.next 开始的子链，拿到“反转后的表头”
            #     ⚠️ 这句就是“self 调用自己”的递归思想：先让更小的同类问题解决好
            newHead = self.reverseList(head.next)

            # 3.2 核心反转：让“后一个节点”的 next 指回“当前节点” → 把箭头翻过来
            #     等价于：head.next.next = head  =>  (后一个).next = 当前
            head.next.next = head

        # 4) 断开当前节点对后一个的旧指针，避免形成环（每层回溯都要断）
        head.next = None

        # 5) 把“最底层返回的表头”（最后一个节点）一路上传（各层都 return 它）
        return newHead

    

