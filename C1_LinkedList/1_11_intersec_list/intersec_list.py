from C1_LinkedList.LNode import LNode

#方法①首尾相接法，就是首尾（连头节点下一个）相连判断是否会相遇
#方法②尾节点法，
def check_intersec(head1, head2):
    if head1 is None or head2 is None or head1.next is None or head2.next is None:
        return None
    tmp1 = head1.next
    n1 = 0
    while tmp1.next is not None:
        tmp1 = tmp1.next
        n1 += 1
    n2 = 0
    tmp2 = head2.next
    while tmp2.next is not None:
        tmp2 = tmp2.next
        n2 += 1
    if tmp1 is tmp2:#尾节点一致，相交
        #长链表先走n1 n2之差步，追击相遇，相遇点即为相交点
        if n1>n2:
            while n1-n2>0:
                head1 = head1.next
                n1 -= 1
        else:#=的情况可以不考虑
            while n2-n1>0:
                head2 = head2.next
                n2 -= 1
        while head2 is not head1:
            head1 = head1.next
            head2 = head2.next
        return head1
    else:
        return None

if  __name__=="__main__":
    i=1
    # 链表头结点
    head1=LNode()
    head1.next=None
    # 链表头结点
    head2=LNode()
    head2.next=None
    tmp=None
    cur=head1
    p=None
    # 构造第1个链表
    while  i<8 :
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        if(i==5) :
            p=tmp
        i +=1
    cur=head2
     # 构造第2个链表
    i=1
    while  i<5:
         tmp=LNode()
         tmp.data=i
         tmp.next=None
         cur.next=tmp
         cur=tmp
         i +=1
    # 使它们相交于结点5
    cur.next=p
    interNode=check_intersec(head1,head2)
    if  interNode==None:
        print("这两个链表不相交：")
    else:
        print("这两个链表相交点为："+str(interNode.data))