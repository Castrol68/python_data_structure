from C1_LinkedList.LNode import LNode

# 构造链表
def constructList():
    i=1
    head=LNode()
    head.next=None
    tmp=None
    cur=head
    # 构造第一个链表
    while  i<8:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i +=1
    cur.next=head.next.next.next#造一个环
    return  head