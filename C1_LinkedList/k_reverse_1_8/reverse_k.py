'''

:function:
    
'''
from C1_LinkedList.LNode import LNode

#逆序无头节点的链表
def reverse(head):
    if head is None or head.next is None:
        return head
    pre = head
    cur = head.next
    next = None
    pre.next = None  # 断开链接
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


def reverse_k(head, k):
    if head is None or head.next is None or k<2:
        return
    i = 1
    pre = head
    begin = head.next
    end = None
    end_next =None
    while begin is not None:
        end = begin
        while i<k:
            if end.next is not None:
                end = end.next
                i += 1
            else:
                return#剩余节点数小于k
        end_next = end.next
        end.next = None#断开链接逆序k个元素内部
        pre.next = reverse(begin)
        begin.next = end_next
        #逆序完成后，回到上次相同的指针状态
        pre = begin
        begin = begin.next
        i = 1




if  __name__=="__main__":
    i=1

    head=LNode()

    head.next=None
    tmp=None
    cur=head
    while  i<8:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1
    print("顺序输出：",end='')
    cur=head.next
    while  cur!=None:
        print(cur.data,end=' ')
        cur=cur.next
    reverse_k(head,3)
    print("\n逆序输出：")
    cur=head.next
    while  cur!=None:
        print(cur.data,end=' ')
        cur=cur.next
    cur=head.next
    while  cur!=None:
        tmp=cur
        cur=cur.next