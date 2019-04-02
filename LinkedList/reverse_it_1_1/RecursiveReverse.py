from LinkedList.reverse_it_1_1.LNode import LNode
#有头节点

def book_recursive_reverse(head):
    if head is None:
        #递归终止条件
        return
    first_node=head.next
    new_head=book_recursive_reverse(first_node)
    head.next=new_head
    return new_head#明显一直返回none

def my_recursive_reverse(head):
    if head is None:
        return head
    elif head.data is None:#是头节点,有头节点其实就稍微区别对待一下就好
        tmp_head=head
        result = my_recursive_reverse(head.next)
        tmp_head.next = result
        return tmp_head
    else:
        if head.next is None: return head #(head.next)下一个节点是none即到了最后一个节点(最大节点)，直接返回最后一个节点
        result = my_recursive_reverse(head.next)#将最大的一直返回，直到放到最前面
        head.next.next = head#head后一个元素指向head自己，逆序
        head.next = None#断开自己与下一个元素的链接
        return result
#  <--
# |   |
# 1   2   3


if __name__ == '__main__':
    i=1
    head=LNode(None)
    head.next=None
    tmp=None
    cur=head
    while i<1:
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
    cur=my_recursive_reverse(head)
    cur = head.next
    print("逆序后：")
    while cur is not None:
        print(cur.data)
        cur=cur.next


