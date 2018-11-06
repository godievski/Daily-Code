# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def serialize(node):
  if (node == None):
    return '-'
  values = [node.val, serialize(node.left), serialize(node.right)]
  return ' '.join(values)


def _deserialize(values, index):  
  val = values[index]
  if(val == '-'):
    return None, index + 1
  left, i = _deserialize(values, index + 1)
  right, j = _deserialize(values, i)
  return Node(val, left, right), j

def deserialize(tree):
  values = tree.split(' ')
  return _deserialize(values, 0)[0]
  

left = Node('left', Node('left.left'))
right = Node('right', None, Node('right.right'))
node = Node('root', left, right)

assert deserialize(serialize(node)).right.right.val == 'right.right'

print('Success!')