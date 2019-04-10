from C1_LinkedList.LNode import LNode


def recursive_remove_dup(head):
    if head.next is None:
        return head
    pre = head
    head.next = recursive_remove_dup(head.next)
    pointer = head.next
    while pointer is not None:
        if head.data == pointer.data:
            pre.next = pointer.next
            pointer = pre.next
        else:
            pointer = pointer.next
            pre = pre.next
    return head

def remove_dup(head):
    if head is None:
        return
    head.next = recursive_remove_dup(head.next)

if __name__ == '__main__':
    i = 1
    head=LNode()
    tmp=None
    cur=head
    while i<2:
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
    remove_dup(head)
    print("删除后：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next