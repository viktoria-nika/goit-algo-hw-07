
# AVL - дерево 

class TreeNode: # реалізуємо один вузол дерева
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree: # реалізуємо двійкове дерево пошуку
    def __init__(self):
        self.root = None

    def insert(self, key): # Методом insert додаємо новий ключ до дерева
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

# Створюємо алгоритм find_max для знаходження максимального значення у дереві, де рухаємось по правих нащадках

    def find_max(self): 
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value
    
# Створюємо алгоритм find_min для знаходження мінімального значення у дереві, рухаючись по лівих нащадках

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value
    
# Функція sum_values: обчислює суму всіх значень у дереві, викликаючи рекурсивний допоміжний метод _sum_values_rec

    def sum_values(self):
        return self._sum_values_rec(self.root)

    def _sum_values_rec(self, node):
        if node is None:
            return 0
        return node.value + self._sum_values_rec(node.left) + self._sum_values_rec(node.right)

# Реалізіція написаних вище функцій:
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [40, 20, 60, 5, 25, 35, 45]
    for value in values:
        bst.insert(value)

    print("Найбільше значення у дереві:", bst.find_max())
    print("Найменше значення у дереві:", bst.find_min())
    print("Сума всіх значень у дереві:", bst.sum_values())
