from C1_LinkedList.LNode import LNode


def reverse(head):
    #判断链表是否为空
    if head is None or head.next is None:
        return
    cur = head.next#对cur与cur.next进行对调
    pre = head
    next_next = None#当前节点的后继节点的后继节点
    while cur is not None and cur.next is not None:
        next_next = cur.next.next
        pre.next = cur.next
        cur.next.next = cur
        cur.next = next_next
        pre = cur
        cur = next_next


if  __name__=="__main__":
    i=1
    head =LNode()
    head.next = None
    tmp = None
    cur = head
    while  i<8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i +=1
    print("顺序输出：")
    cur = head.next
    while cur != None:
        print(cur.data,end=' ')
        cur = cur.next
    reverse (head)
    print("\n逆序输出：")
    cur = head.next
    while  cur != None:
        print(cur.data,end=' ')
        cur = cur.next
    cur = head.next
    while  cur != None:
        cur = cur.next

