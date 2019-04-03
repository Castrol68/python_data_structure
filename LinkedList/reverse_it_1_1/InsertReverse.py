from LinkedList.LNode import LNode


def book_reverse(head):
    if head is None or head.next is None:
        return
    cur = None
    next = None

    cur = head.next.next
    head.next.next = None

    while cur is not None:
        next=cur.next
        cur.next=head.next
        head.next=cur
        cur=next


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

    book_reverse(head)
    print("逆序后：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur=cur.next

