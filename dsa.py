class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    # def printLinkedList(self):
    #     current_node = self.head
    #     while current_node:
    #         print(current_node.data)
    #         current_node = current_node.next

    def remove_beginning(self):
        if not self.head:
            return None

        removed_data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed_data

    def remove_at_end(self):
        if not self.head:
            return None

        removed_data = self.tail.data
        current_node = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            while current_node.next != self.tail:
                current_node = current_node.next

            current_node.next = None
            self.tail = current_node

        return removed_data

    def remove_at(self, data):
        if not self.head:
            return None
        
        if self.head.data == data:
            return self.remove_beginning()

        current_node = self.head
        previous_node = None

        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return None

        if current_node == self.tail:
            self.tail = previous_node

        removed_data = current_node.data
        previous_node.next = current_node.next

        return removed_data

    def insert_after(self, nodedata, data):
        new_node = Node(data)
        current_node = self.head
        
        while current_node and current_node.data != nodedata:
            current_node = current_node.next

        if current_node is None:
            return False

        new_node.next = current_node.next

        current_node.next = new_node

        if current_node == self.tail:
            self.tail = new_node

        return True

    def to_list(self):
        data = []
        current_node = self.head
        while current_node:
            data.append(current_node.data)
            current_node = current_node.next
        return data





