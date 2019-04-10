from C1_LinkedList.LNode import LNode
def  printList(head):
    cur=head.next
    while  cur!=None:
        print(cur.data,end=' ')
        cur=cur.next


def remove_node(p):
    if p.next is None or p is None:
        return False#无法删除
    p_next = p.next
    next = p.next.next
    p.data = p_next.data
    p.next = next
    p_next.next = None
    return True


if  __name__=="__main__":
    i=1
    head=LNode() # 链表头结点
    head.next=None
    tmp=None
    cur=head
    p=None
    # 构造链表
    while  i<8:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        if  i==5:
            p=tmp
        i +=1
    print("删除结点"+str(p.data)+"前链表: ")
    printList(head)
    result=remove_node(p)
    if  result:
        print("\n删除该结点后链表:",end=' ')
        printList(head)
