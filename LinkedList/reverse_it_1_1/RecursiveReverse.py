from LinkedList.reverse_it_1_1.LNode import LNode


def book_recursive_reverse(head):
    if head is None:
        #递归终止条件
        return
    first_node=head.next
    new_head=book_recursive_reverse(first_node)
    head.next=new_head
    return new_head#明显一直返回none

def my_recursive_reverse(rest):
    if rest.next is None:
        return rest
    new_head = my_recursive_reverse(rest.next)
    new_head.next=rest
    rest.next=None
    return new_head




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
    # cur = book_recursive_reverse(head)
    cur=my_recursive_reverse(head.next)
    # cur = head.next
    print("逆序后：")
    while cur is not None:
        print(cur.data)
        cur=cur.next


