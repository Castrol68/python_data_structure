# 双重循环即可
from LinkedList.LNode import LNode


def book_remove_dup(head):
    if head is None or head.next is None:
        return
    out_cur = head.next
    inner_cur = None
    inner_pre = None
    while out_cur is not None:
        inner_cur = out_cur.next
        inner_pre = out_cur
        while inner_cur is not None:
            if inner_cur.data == out_cur.data:
                inner_pre.next = inner_cur.next
            else:
                inner_pre = inner_cur
            inner_cur = inner_cur.next
        out_cur = out_cur.next


if __name__ == '__main__':
    i = 1
    head=LNode()
    tmp=None
    cur=head
    while i<7:
        tmp=LNode()
        if i%2==0:
            tmp.data=i+1
        elif i%3==0:
            tmp.data=i-2
        else:
            tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1
    print("删除前：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    book_remove_dup(head)
    print("删除后：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next


