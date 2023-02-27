# Singly LinkedList Implementation
class Node():
    """ A node has data and a pointer to next node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class CustomLinkedList():
    """ A LinkedList has a head node and chain of nodes """
    def __init__(self, data):
        x = Node(data)
        self.head = x

    # Traversal of linked list
    def traversal(self):
        temp = self.head
        while (temp!= None):
            print(f" --> {temp.data}",end='')
            temp = temp.next

    # Lookup
    def lookup(self, node):
        if self.head == None:
            print("No nodes")
        else:
            temp = self.head
            while (temp.next.data!=node.data):
                temp = temp.next
            return temp.next.data

    # Insertion has 3 cases:
    # At the beginning of the list
    def insert_beginning(self, node):
        node.next = self.head
        self.head = node
        print(f"Inserted {self.head.data} as head node...")

    # At the end of the list
    def insert_end(self, node):
        temp = self.head
        while temp.next!= None:
            temp = temp.next
        temp.next = node
        print(f"Appended {temp.next.data} as tail node...")

    # Midway at position pos
    def insert_at_pos(self, node, pos):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            for _ in range(pos-1) :
                temp = temp.next
            node.next = temp.next
            temp.next = node
            print(f"Inserted {temp.next.data} at position {pos}...")

    # Deletion
    def deletion(self, node):
        if self.head == None:
            print("No nodes to delete")
        else:
            temp = self.head
            while (temp!= None):
                # print("Temp.next",temp.next)
                # print("Node",node)
                if temp.next.data == node.data:
                    temp.next = temp.next.next
                    print(f"Deleting {node.data}...")
                    del node
                    break
                temp = temp.next





x = CustomLinkedList(5)
x.insert_beginning(Node(4))
x.insert_beginning(Node(3))
x.insert_beginning(Node(2))
x.insert_beginning(Node(1))
x.insert_end(Node(6))
x.insert_end(Node(7))
x.insert_at_pos(Node(90),2)
x.traversal()

print()
x.deletion(Node(4))
x.deletion(Node(90))
x.traversal()
