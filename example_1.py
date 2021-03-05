class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def search(self,target):
        if self.data == target:
            print("Found it")
            return self
        
        if self.left and self.data > target:
            return self.left.search(target)
        
        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not in tree")
    
    def traversePreorder(self):

        print(self.data)
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()
    def traverseInorder(self):
        print(self.data)
        if self.left:
            self.left.traversePreorder()
            print(self.data)
        if self.right:
            self.right.traversePreorder()
    def traversePostorder(self):
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()
            print(self.data)




class Tree:
    def __init__(self,root, name=''):
        self.root = root
        self.name = name
    def seach(self, target):
        return self.root.search(target)
    def traverseInorder(self):
        self.root.traverseInorder()
    def traversePreorder(self):
        self.root.traversePreorder()
    def traversePostorder(self):
        self.root.traversePostorder()

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(3)
node.left.right = Node(6)

node.right.right = Node(25)
node.right.left = Node(20)

# print(node.right.data)
# print(node.right.right.data)

newTree = Tree(node, "New Tree")


# print(newTree.root.right.right.data)

found = newTree.root.search(20)

# print(found.data)

# newTree.traverseInorder()
newTree.traversePostorder()
# newTree.traversePreorder()