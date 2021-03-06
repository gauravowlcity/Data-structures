class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =  None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def addTwoLists(self,first,second):
        prev = temp = None
        carry  = 0
        while (first is not None or second is not None):
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data

            sum = carry +fdata +sdata

            carry = 0 if sum<10 else 1

            sum= sum if sum<10 else sum%10

            temp = Node(sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next  =temp

            prev = temp

            if first is not None:
                first = first.next

            if second is not None:
                second = second.next

        if carry >0:
            temp.next = Node(carry)

    def printList(self):
        curr = self.head
        while curr:
            print curr.data
            curr= curr.next



firstLinkedList = LinkedList()
secondLinkedList = LinkedList()
firstLinkedList.push(5)
firstLinkedList.push(6)
firstLinkedList.push(3)
firstLinkedList.push(5)
firstLinkedList.push(7)

print "first LinkedList is"
firstLinkedList.printList()

secondLinkedList.push(4)
secondLinkedList.push(5)

print "second list is "
print secondLinkedList.printList()

res = LinkedList()
res.addTwoLists(firstLinkedList.head,secondLinkedList.head)
print "Resultant list is "
res.printList()
