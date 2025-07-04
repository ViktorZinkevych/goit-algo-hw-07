class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_value(root):
    if root is None:
        return None

    current = root
    while current.left:
        current = current.left
    return current.value

# Приклад створення дерева
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)

print("Найменше значення в дереві:", find_min_value(root))