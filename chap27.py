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

#
# functions
#

def print_tree(tree):
    if tree is None: return
    print(tree.cargo, end = " ")
    print_tree(tree.left)
    print_tree(tree.right)

def print_tree_postorder(tree):
    if tree is None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end = " ")

def print_tree_inorder(tree):
    if tree is None: return
    print_tree_inorder(tree.left)
    print(tree.cargo, end = " ")
    print_tree_inorder(tree.right)

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list)
        if not get_token(token_list, ")"):
            raise ValueError("Missing close parenthesis")
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return TreeNode(x, None, None)

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product(token_list)
        return TreeNode("*", a, b)
    return a

def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return TreeNode("+", a, b)
    return a

def create_token_list(r_inpt):
    r_inpt = r_inpt.strip()
    temp_token_list = [char for char in r_inpt]
    token_list = []
    for i in range(len(temp_token_list)):
        if temp_token_list[i] != " ":
            if temp_token_list[i].isdigit():
                token_list.append(int(temp_token_list[i]))
            else:
                token_list.append(temp_token_list[i])
    return token_list


three = TreeNode(4, TreeNode(5), TreeNode(5))
two1 = TreeNode(2, three, TreeNode(4))
two2 = TreeNode(2, TreeNode(4), TreeNode(4))
one = TreeNode(1, two1, two2)
print(one.total())
print(one.depth())

tree = TreeNode("+", TreeNode(1), TreeNode("*", TreeNode(2), TreeNode(3)))

print_tree(tree)
print()
print_tree_postorder(tree)
print()
print_tree_inorder(tree)
print()


token_list = [9, "*", 11, "end"]

x = get_number(token_list)
print_tree_postorder(x)
print()
print(token_list)
9, "*", 11, "end"
token_list = [2, "*", 3, "*", 5, "*", 7, "end"]

tree = get_product(token_list)
print_tree_postorder(tree)
print()

token_list = [9, "*", 11, "+", 5, "*", 7, "end"]
tree = get_sum(token_list)
print_tree_postorder(tree)
print()

token_list = [9, "*", "(", 11, "+", 5, ")", "*", 7, "end"]
tree = get_sum(token_list)
print_tree_postorder(tree)
print()

token_list = [9, "*", "(", "(", 11, "+", 5, ")", "*", "(", 8, "+", 2, ")", ")", "*", 7, "end"]
tree = get_sum(token_list)
print_tree_postorder(tree)
print()

string = "1*( 2+ 3)*7"
token_list = create_token_list(string)
print(token_list)
