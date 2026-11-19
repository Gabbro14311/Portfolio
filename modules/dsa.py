class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def _normalize(self, value):
        if value is None:
            return ""
        return str(value).strip()

    def insert_at_beginning(self, data):
        if not self._normalize(data):
            return False

        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        return True

    def insert_at_end(self, data):
        if not self._normalize(data):
            return False

        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        return True

    def search(self, data):
        target = self._normalize(data)
        if not target:
            return False

        current_node = self.head
        while current_node:
            if self._normalize(current_node.data) == target:
                return True
            current_node = current_node.next
        return False

    # def print_linked_list(self):
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
        target = self._normalize(data)
        if not self.head or not target:
            return None

        if self._normalize(self.head.data) == target:
            return self.remove_beginning()

        current_node = self.head
        previous_node = None

        while current_node and self._normalize(current_node.data) != target:
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
        target = self._normalize(nodedata)
        if not target or not self._normalize(data):
            return False

        new_node = Node(data)
        current_node = self.head

        while current_node and self._normalize(current_node.data) != target:
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

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if data is None or str(data).strip() == "":
            return False

        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node
        return True

    def pop(self):
        if self.top:
            removed_node = self.top
            self.top = self.top.next
            removed_node.next = None
            return removed_node.data

        return None

    def peek(self):
        if self.top:
            return self.top.data

        return None

    # def print_stack(self):
    #     current_node = self.top
    #     while current_node:
    #         print(current_node.data)
    #         current_node = current_node.next

    def is_empty(self):
        if self.top is not None:
            return False

        return True

    def to_list(self):
        data = []
        current_node = self.top
        while current_node:
            data.append(current_node.data)
            current_node = current_node.next
        return data

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if data is None or str(data).strip() == "":
            return False

        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        return True

    def dequeue(self):
        if self.head is not None:
            removed_node = self.head
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            removed_node.next = None
            return removed_node.data

        return None

    def is_empty(self):
        if self.head is not None:
            return False

        return True

    def get_size(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next

        return size

    # def print_queue(self):
    #     current_node = self.head
    #     while current_node:
    #         print(current_node.data)
    #         current_node = current_node.next

    def to_list(self):
        data = []
        current_node = self.head
        while current_node:
            data.append(current_node.data)
            current_node = current_node.next
        return data

class ReverseStrings:
    def __init__(self, string):
        self.string = string
        self.reversed = Stack()

    def reverse(self):
        for char in self.string:
            self.reversed.push(char)

        return "".join(self.reversed.to_list())


class InfixToPostfix:
    def __init__(self, equation):
        self.equation = equation
        self.operators = Stack()
        self.output = Stack()

    def parse(self):
        cleaned_input = self.equation.replace(" ", "")

        for operator in ["+", "-", "*", "/", "^", "(", ")"]:
            cleaned_input = cleaned_input.replace(operator, f" {operator} ")

        tokens = cleaned_input.split()
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

        while tokens:
            token = tokens.pop(0)

            if token.isalnum():
                self.output.push(token)

            elif token == "(":
                self.operators.push(token)

            elif token == ")":
                while not self.operators.is_empty() and self.operators.peek() != "(":
                    self.output.push(self.operators.pop())

                self.operators.pop()

            elif token in precedence:
                while not self.operators.is_empty() and self.operators.peek() in precedence and precedence[self.operators.peek()] >= precedence[token]:
                    self.output.push(self.operators.pop())

                self.operators.push(token)

        while not self.operators.is_empty():
            self.output.push(self.operators.pop())

        return " ".join(reversed(self.output.to_list()))