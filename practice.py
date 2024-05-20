class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
        self.head = new_node

    def insert_at_index(self, index, data):
        new_node = Node(data)
        current_node = self.head
        if self.head is None:
            self.insert_at_beginning(data)
            self.tail = new_node
            return
        for i in range(1, index - 1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        if new_node is not None:
            current_node.next.prev = new_node
        if new_node is None:
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        current_node = self.head
        if self.head is None:
            self.insert_at_beginning(data)
            self.tail = new_node
            return
        while current_node.next:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        self.tail = new_node

    def remove_first_node(self):
        if self.head is None:
            print("LinkedList is empty!")
            return
        self.head = self.head.next

    def remove_at_index(self, index):
        current_node = self.head
        if self.head == index:
            self.remove_first_node()
            return
        for i in range(1,index):
            current_node = current_node.next
        if current_node is not None:
            current_node.next = current_node.next.next

    def remove_last_node(self):
        current_node = self.head
        previous_node = None
        if self.head is None:
            print("Linkedlist is empty!")
            return
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        if previous_node.next is not None:
            previous_node.next = None

    def linkedlist_traversal_forward(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data}<==>", end=" ")
            current_node = current_node.next
        print("\r")

    def linkedlist_traversal_backward(self):
        current_node = self.tail
        if self.head is None:
            print("Linkedlist is empty!")
            return
        while current_node is not None:
            print(f"{current_node.data}<==>", end=" ")
            current_node = current_node.prev
        print("\r")


dll = LinkedList()
dll.head = Node(0)
second = Node(2)
third = Node(3)
first = dll.head
dll.tail = third
first.next = second
second.prev = first
second.next = third
third.prev = second
dll.insert_at_end(4)
dll.insert_at_beginning(1)
dll.insert_at_index(6, 6)
dll.linkedlist_traversal_backward()
dll.linkedlist_traversal_forward()
dll.remove_last_node()
dll.remove_first_node()
dll.remove_at_index(3)
dll.linkedlist_traversal_forward()
