class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_tree(root):
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

# Приклад створення дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

print("Сума всіх значень у дереві:", sum_tree(root))