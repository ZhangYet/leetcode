class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recur_tree(root):
    if root.left is None and root.right is None:
        return root.val
    elif root.left is None:
        return [str(root.val), 'None', recur_tree(root.right)]
    elif root.right is None:
        return [str(root.val), recur_tree(root.left), 'None']
    else:
        return [str(root.val), recur_tree(root.left), recur_tree(root.right)]

def recur_list(list):
    root = TreeNode(int(list[0]))
    if list[1] != 'None':
        root.left = recur_list(list[1])
    if list[2] != 'None':
        root.right = recur_list(list[2])
    return root
    
class Codec:

    def serialize(self, root):
        res = str(recur_tree(root))
        return res

    def deserialize(self, data):
        data = eval(data)
        return recur_list(data)

def test():
    root = TreeNode(0)
    left1 = TreeNode(1)
    right1 = TreeNode(2)
    root.left = left1
    root.right = right1
    left2 = TreeNode(3)
    right2 = TreeNode(4)
    right1.left = left2
    right1.right = right2
    left3 = TreeNode(5)
    left2.left = left3
    t = Codec()
    res = t.serialize(root)

    
test()