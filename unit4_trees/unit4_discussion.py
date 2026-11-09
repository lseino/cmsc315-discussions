"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The helper compares values at each level. Smaller values belong in
        # the left subtree and larger values belong in the right subtree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # A missing reference is the insertion point for a new leaf node.
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Equal values are ignored so the tree stores each employee ID once.

        # Returning node reconnects this subtree to its parent after recursion.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A comparison can discard an entire subtree. A balanced BST therefore
        # searches in O(log n) time on average instead of scanning every item.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reaching None means the value is not present in this search path.
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # Every left value is smaller and every right value is larger, so
        # visiting left, node, then right produces ascending sorted output.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION: EMPLOYEE DIRECTORY ===")
    employee_ids = [1050, 1025, 1075, 1010, 1040, 1060, 1090]
    employee_tree = BST()

    # This order creates left and right branches instead of a one-sided chain.
    # Each comparison chooses only one subtree, reducing the remaining search
    # space when the tree stays reasonably balanced.
    for employee_id in employee_ids:
        employee_tree.insert(employee_id)
        print(f"Inserted employee ID: {employee_id}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_ids = employee_tree.inorder()
    print(f"Employee IDs in sorted order: {sorted_ids}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # Existing IDs return True; missing IDs follow their possible branch until
    # the recursion reaches None and then return False.
    for target in (1010, 1075, 1000, 1100):
        print(f"Employee ID {target} found: {employee_tree.search(target)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    empty_tree = BST()
    print(f"Empty-tree traversal: {empty_tree.inorder()}")
    print(f"Search empty tree for 1050: {empty_tree.search(1050)}")

    # Duplicate IDs are ignored, preventing ambiguous duplicate records.
    employee_tree.insert(1050)
    print(f"After duplicate 1050 insertion: {employee_tree.inorder()}")

    single_node_tree = BST()
    single_node_tree.insert(2000)
    print(f"Single-node traversal: {single_node_tree.inorder()}")

    # Sequential insertion demonstrates the main BST performance limitation:
    # it creates a right-skewed tree that behaves like a linked list.
    skewed_tree = BST()
    for employee_id in (1001, 1002, 1003, 1004):
        skewed_tree.insert(employee_id)
    print(f"Sequential IDs create sorted but skewed output: {skewed_tree.inorder()}")


if __name__ == "__main__":
    main()
