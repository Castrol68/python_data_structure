from LinkedList.LNode import LNode


def find_lask_k(head, k):
    if head is None or head.next is None:
        return head
    slow = LNode()
    fast = LNode()
    slow = head.next
    fast = head.next
    i = 0
    while i<k and fast is not None:
        fast=fast.next
        i+=1
    if i<k:#不够长
        return None
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


# 构造一个单链表
def ConstructList():
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    # 构造第一个链表
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    return head


# 顺序打印单链表结点的数据
def PrintList(head):
    cur = head.next
    while cur != None:
        print(cur.data,end=' ')
        cur = cur.next

if  __name__=="__main__":
    head=ConstructList()	# 链表头指针
    result=None
    print('链表：',end=' ')
    PrintList(head)
    result=find_lask_k(head,3)
    if  result!=None:
        print("\n链表倒数第3个元素为："+str(result.data))




