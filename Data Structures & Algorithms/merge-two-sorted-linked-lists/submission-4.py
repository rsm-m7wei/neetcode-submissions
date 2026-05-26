# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


        # 🧩 Definition for singly-linked list（单链表的定义）
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val       # 当前节点的值
#         self.next = next     # 指向下一个节点的指针

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # 🧠 1️⃣ 创建一个假头节点 dummy
        # # 它不存储真实数据，只是为了方便记录新链表的起点
        # dummy = ListNode()

        # # 🧠 2️⃣ tail 指针用来操作新链表的“尾巴”
        # # 每次我们接上一个节点后，tail 都会往后移动
        # tail = dummy

        # # 🧩 3️⃣ 当两个链表都没走完时，比较当前节点的值
        # while list1 and list2:
        #     # 如果 list1 的当前节点值更小，就把它接到 tail 后面
        #     if list1.val < list2.val:
        #         tail.next = list1     # 把 list1 当前节点接到结果链表后
        #         list1 = list1.next    # list1 指针往后移一格
        #     else:
        #         tail.next = list2     # 否则接上 list2 当前节点
        #         list2 = list2.next    # list2 指针往后移一格
        #     tail = tail.next          # 无论接谁，tail 都要往后移一格

        # # 🧩 4️⃣ 如果有一个链表已经走完，直接把另一个链表剩余的部分接上
        # # 因为两个链表都是有序的，剩下的那部分已经是有序的
        # if list1:
        #     tail.next = list1
        # elif list2:
        #     tail.next = list2

        # # 🧩 5️⃣ 返回合并后链表的头节点
        # # dummy 是假头，所以要返回 dummy.next
        # return dummy.next
        

        # #首先创建一个空的节点当作头
        # head =ListNode(None)
        # #指向这个空节点
        # curr = head
        # #接着处理两个list
        # while list1 or list2:
        #     #如果其中一个结束了就指向另一个，并且可以返回列表头
        #     if not list1:
        #         curr.next =list2
        #         return head.next
        #     if not list2:
        #         curr.next=list1
        #         return head.next
        #     #两个都有的时候就比较大小来处理
        #     if list1.val<list2.val:
        #         curr.next = list1
        #         list1 =list1.next
        #     elif list1.val>=list2.val:
        #         curr.next =list2
        #         list2 =list2.next
        #     #不要忘记我们还要移动curr
        #     curr =curr.next
        # return head.next


        #创建一个空的指针指向当前的第一个节点
        #还需要创建一个不变的来储存投
        head =ListNode(None)
        #一个动的指针指向第一个头
        curr = head
        #当两个中有一个还在的时候就可以继续处理
        while list1 or list2:
            #考虑特殊情况一个没有的时候
            #这里不用写head，直接写list就行，就会默认是第一个
            if not list1:
                curr.next =list2
                return head.next
            if not list2:
                curr.next =list1
                return head.next
            #两个都有的时候
            if list1.val<list2.val:
                curr.next =list1
                #别忘了要更新每一个链表的数值,并且移动curr的指针
                list1 =list1.next
                curr =curr.next
            elif list2.val<=list1.val:
                curr.next=list2
                curr =curr.next
                list2=list2.next
        return head.next
