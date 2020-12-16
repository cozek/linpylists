from singly_linked_list import SinglyLinkedList, Node

# def main1():


#     vals = [4,5,8,1,2,-1]
#     llist = LinkedList()

#     for num in vals:
#         llist.append(num)


#     print(llist)
#     print(llist[5])
#     print(len(llist))

#     llist[2] = 10

#     node = Node(5)
#     print(node)

def main2():
    sll = SinglyLinkedList()
    for i in range(1,10):
        sll.append(i)
    print(sll)
    print(len(sll))
    sll[-9] = 100
    print(sll[7])
    print("~~~~~~~~")
    print(sll)
    print(len(sll))
    
    while(sll):
        sll.pop()
        print(sll)
    # print(sll.tail)

def test_remove():
    sll = SinglyLinkedList()
    arr = [1,2,3,4,5,5,8,9]
    for i in arr:
        sll.append(i)
    print(sll)

    # sll.remove(1)
    # print(sll)
    sll.remove(11)
    print(sll)
    print(sll.tail)
    print(sll.head)


if __name__ == '__main__':
    test_remove()
