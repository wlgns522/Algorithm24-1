class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(n):
    if n is not None :
        print(n.data, end= ' ')
        preorder(n.left)
        preorder(n.right)
d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d,e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root =  TNode('A', b, c)

print('  Pre-Order : ', end='')
preorder(root)
print()
