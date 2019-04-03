from LinkedList.LNode import LNode


def add(h1, h2):
    if h1 is None or h1.next is None:
        return h2
    if h2 is None or h2.next is None:
        return h1

    c=0#记录进位
    sums=0#记录两个节点相加的值

    p1=h1.next
    p2=h2.next

    tmp=None#存储相加的和
    resultHead=LNode()#相加后的链表的头节点
    resultHead.next=None

    p=resultHead#用来指向链表resultHead最后一个节点
    while p1 is not None and p2 is not None:
        tmp=LNode()
        sums=p1.data + p2.data + c
        tmp.data=sums % 10
        c=int(sums/10)

        p.next = tmp#加入新链表
        p=tmp

        p1=p1.next
        p2=p2.next
    #p2比p1长,p1比p2长
    if p1 is None:
        while p2 is not None:
            tmp=LNode()
            sums=p2.data+c
            tmp.data=sums%10
            c=int(sums/10)
            p.next=tmp
            p=tmp
            p2=p2.next
    if p2 is None:
        while p1 is not None:
            tmp=LNode()
            sums=p1.data+c
            tmp.data=sums%10
            c=int(sums/10)
            p.next=tmp
            p=tmp
            p1=p1.next
    #完成全部计算后还有进位
    if c==1:
        tmp=LNode()
        tmp.data=1
        p.next=tmp
    return resultHead

if __name__ == '__main__':
    i = 1
    head1 = LNode()
    head1.next = None
    head2 = LNode()
    head2.next = None
    tmp = None
    cur = head1
    addResult = None
    # 构造第一个链表
    while i < 7:
        tmp = LNode()
        tmp.data = i + 2
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    cur = head2
    # 构造第二个链表
    i = 9
    while i > 4:
        tmp = LNode()

        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i -= 1
    print("\nHead1: ",end='')

    cur = head1.next
    while cur is not None:
        print(cur.data,end='')
        cur = cur.next
    print("\nHead2: ",end='')
    cur = head2.next
    while cur is not None:
        print(cur.data,end='')
        cur = cur.next
    addResult = add(head1, head2)
    print("\n相加后: ",end='')
    cur = addResult.next
    while cur is not None:
        print(str(cur.data),end='')
        cur = cur.next





