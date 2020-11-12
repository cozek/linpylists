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
    print(sll[-9])
    print(sll[1:3])

if __name__ == '__main__':
    main2()
