class Tree:

    def __init__(self):
        self.root = None

    def __str__(self):
        return (str(self.root))


class TreeNode:

    def __init__(self, cargo=None, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self, level=0):
        string = "\t"*level + str(self.cargo) + "\n"
        if self.left:
            string += self.left.__str__(level+1)
        if self.right:
            string += self.right.__str__(level+1)
        return string

    def total(self):
        if isinstance(self.cargo, int):
            left = 0
            right = 0
            if self.left is not None:
                left = self.left.total()
            if self.right is not None:
                right = self.right.total()

            return left + right + self.cargo
        else:
            return 0

    def depth(self, d=0):
        left = 0
        right = 0
        if self.left is not None:
            left = self.left.depth(d+1)
        if self.right is not None:
            right = self.right.depth(d+1)

        return max(d, left, right)


three = TreeNode(4, TreeNode(5), TreeNode(5))
two1 = TreeNode(2, three, TreeNode(4))
two2 = TreeNode(2, TreeNode(4), TreeNode(4))
one = TreeNode(1, two1, two2)
print(one.total())
print(one.depth())
