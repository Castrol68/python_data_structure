from LinkedList.LNode import LNode

def my_reverse(head):
    if head==None or head.next==None or head.next.next==None:#书上代码有误，无法应对1个元素的边界情况
        return
    pre=None
    cur=None
    next=None
    pre=head.next
    cur=head.next.next
    next=cur
    pre.next=None#断开链接防止互指

    while cur.next is not None:
        next=cur.next#防止链表只有头节点和一个元素的情况
        cur.next=pre
        pre=cur
        cur=next

    cur.next=pre#最后一个节点指向倒数第二个节点
    head.next=cur

def book_reverse(head):
    if head==None or head.next==None:
        return
    pre=None
    cur=None
    next=None

    cur=head.next
    next=cur.next
    cur.next=None
    pre=cur
    cur=next

    while cur.next!=None:
        next=cur.next
        cur.next=pre
        pre=cur
        cur=cur.next
        cur=next

    cur.next = pre  # 最后一个节点指向倒数第二个节点
    head.next = cur


if __name__ == '__main__':
    i=1
    head=LNode(None)
    head.next=None
    tmp=None
    cur=head
    while i<8:
        tmp=LNode(i)
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1
    print("逆序前：")
    cur=head.next
    while cur is not None:
        print(cur.data)
        cur=cur.next

    my_reverse(head)
    print("逆序后：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur=cur.next
