from C1_LinkedList.LNode import LNode

#返回链表中间节点
def find_middle_node(head):
    if head is None or head.next is None:
        return head
    fast = head#每次向前走两步
    slow = head#每次向前走一步
    pre_slow = head

    while fast is not None and fast.next is not None:
        pre_slow=slow
        slow=slow.next
        fast=fast.next.next#走两步
    pre_slow.next=None#断开成两个独立链表
    return slow

#对不带头结点的进行翻转
def reverse(head):
    if head is None or head.next is None:
        return head
    pre = head
    cur = head.next
    next = cur.next
    pre.next = None

    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur=next
    return pre

def reorder(head):
    if head is None or head.next is None or head.next.next is None:#只有一个元素的情况①
        return
    cur1 = head.next
    mid = find_middle_node(head.next)
    cur2 = reverse(mid)
    tmp = None

    while cur1.next is not None:
        tmp = cur1.next
        cur1.next = cur2
        cur1 = tmp

        tmp = cur2.next
        cur2.next = cur1#如果只有一个元素这个会让cur1指向自己
        cur2 = tmp
    cur1.next = cur2
    cur2.next = None#只有一个元素的情况②

if  __name__=="__main__":
    i=1
    head=LNode()
    head.next=None
    tmp=None
    cur=head
    # 构造第一个链表
    while i<2 :
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i +=1

    print("排序前： ",end='')
    cur=head.next
    while cur!=None:
        print(cur.data,end='')
        cur=cur.next
    reorder(head)
    print("\n排序后： ",end='')
    cur=head.next
    while cur is not None:
        print(cur.data,end='')
        cur=cur.next