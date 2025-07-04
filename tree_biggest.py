class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_value(root):
    if root is None:
        return None

    current = root
    while current.right:
        current = current.right
    return current.value

# Приклад створення дерева та виклик функції
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)

print("Найбільше значення в дереві:", find_max_value(root))