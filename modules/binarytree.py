class Node:
    """A node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """A binary tree data structure."""
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def set_root(self, value):
        """Set or replace the root node of the binary tree."""
        if value is None or str(value).strip() == "":
            self.root = None
            return None
        new_root = Node(value)
        new_root.left = self.root
        self.root = new_root
        return self.root

    def search(self, target):
        """Search for a node whose string value matches target; return the Node or None."""
        target_str = str(target)

        def _search(node):
            if not node:
                return None
            if str(node.value) == target_str:
                return node
            return _search(node.left) or _search(node.right)

        return _search(self.root)

    def delete_node(self, target):
        """Delete a node matching target; promote from left subtree first when two children exist."""
        target_str = str(target)
        deleted = [False]

        def _detach_max_right(node):
            if not node.right:
                return node.value, node.left
            max_val, updated_right = _detach_max_right(node.right)
            node.right = updated_right
            return max_val, node

        def _delete(node):
            if not node:
                return None

            if str(node.value) == target_str:
                deleted[0] = True
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                # Left-first promotion: take rightmost descendant of node.left
                left_val, updated_left = _detach_max_right(node.left)
                node.value = left_val
                node.left = updated_left
                return node

            node.left = _delete(node.left)
            node.right = _delete(node.right)
            return node

        self.root = _delete(self.root)
        return deleted[0]

    def insert_left(self, current_node, value):
        """Insert a node as the left child of the current node."""
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        """Insert a node as the right child of the current node."""
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def preorder_traversal(self, start, traversal):
        """Traverse the tree in preorder (root, left, right)."""
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        """Traverse the tree in inorder (left, root, right)."""
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        """Traverse the tree in postorder (left, right, root)."""
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + " ")
        return traversal

    def count_nodes(self):
        """Return total number of nodes in the binary tree."""
        def _count(node):
            if not node:
                return 0
            return 1 + _count(node.left) + _count(node.right)

        return _count(self.root)

    def height(self):
        """Return height of the binary tree (0 if empty)."""
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def to_levels(self):
        """Group nodes level-by-level with unique node and parent IDs using plain lists."""
        if not self.root:
            return []

        levels = []
        next_id = 0
        root_id = next_id
        next_id += 1

        current_queue = [(self.root, "ROOT", root_id, None)]

        while current_queue:
            level_items = []
            next_queue = []

            for node, relation, node_id, parent_id in current_queue:
                level_items.append({
                    "id": node_id,
                    "parent_id": parent_id,
                    "value": node.value,
                    "relation": relation,
                })

                if node.left:
                    left_id = next_id
                    next_id += 1
                    next_queue.append((node.left, f"L:{node.value}", left_id, node_id))

                if node.right:
                    right_id = next_id
                    next_id += 1
                    next_queue.append((node.right, f"R:{node.value}", right_id, node_id))

            levels.append(level_items)
            current_queue = next_queue

        return levels

def build_tree_from_sequence(values):
    """Build a level-order binary tree using insert_left and insert_right."""
    if not values:
        return BinaryTree(None)

    tree = BinaryTree(values[0])
    nodes_queue = [tree.root]
    idx = 1

    while nodes_queue and idx < len(values):
        current = nodes_queue.pop(0)

        if idx < len(values):
            left_val = values[idx]
            idx += 1
            if left_val is not None:
                tree.insert_left(current, left_val)
                nodes_queue.append(current.left)

        if idx < len(values):
            right_val = values[idx]
            idx += 1
            if right_val is not None:
                tree.insert_right(current, right_val)
                nodes_queue.append(current.right)

    return tree