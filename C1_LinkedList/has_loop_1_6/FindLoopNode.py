from C1_LinkedList.LNode import LNode
from C1_LinkedList.has_loop_1_6.ContainsLoop import constructList


def has_loop(head):
    if head is None or head.next is None:
        return
    slow = fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return

def my_has_loop(head)->bool:
    #破坏型判断是否有环
    if head is None or head.next is None:
        return False
    cur = head.next
    flag = LNode(0)
    while cur:
        if cur.next is flag:
            return True
        temp = cur.next
        cur.next = flag
        cur = temp
    return False

def find_loop_node(head, meet_node):
    first = head.next
    second = meet_node
    while first != second:
        first = first.next
        second = second.next
    return first

if __name__ == '__main__':
    head = constructList()  # 头结点
    meetNode = has_loop(head)
    loopNode = None
    if meetNode != None:
        print("有环")
        loopNode = find_loop_node(head, meetNode)
        print("环的入口点为：" + str(loopNode.data))
    else:
        print("无环")