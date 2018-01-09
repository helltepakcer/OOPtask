
"""
 #2. Create LinkedList Class with methods:
 #a) get(i)


(el) - first element = el

 """

class Node:
    def __init__( self, data ) :
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        node = self.head
        count = 0
        while node.next != None:
            if count == index:
                return node.data
            else:
                count +=1
                node = node.next
        return("There is error occurred process")
    # b) put(i)
    def put(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
# e) size()
    def size(self):
        node = self.head
        size = 0
        while node.next != None:
            size += 1
            node = node.next
        return size

    # d) indexOf
    def indexOf(self,k):
        p = self.head
        if p != None:
            while p.next != None:
                if (p.data == k):
                    return p
                p = p.next
            if (p.data == k):
                return p
        return None

    # c) delete(i)
    def delete(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

