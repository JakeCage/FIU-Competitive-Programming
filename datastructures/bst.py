# Binary Search Tree in Python


class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def rmvLowestChild(self):  # returns the child aswell
        if self.leftChild:
            return self.leftChild.rmvLowestChild()
        else:
            tmp = self.leftChild
            self.leftChild = None
            return tmp

    def preorder(self):
        if self:
            if self.value:
                print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            if self.value:
                print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            if self.value:
                print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

    def reversedOrder(self):
        if self:
            if self.rightChild:
                self.rightChild.reversedOrder()
            if self.value:
                print(str(self.value))
            if self.leftChild:
                self.leftChild.reversedOrder()

    def getLowestChild(self):
        if self.leftChild:
            return self.leftChild.getLowestChild()
        return self.value


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        self.root = Node(data)
        return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        return False

    def find(self, val):
        if self.root:
            return self.root.remove(val)
        return False

    def remove(self, val):
        if self.root:
            curr = self.root

            while curr and curr.value != val:
                if curr.value > val:
                    curr = curr.leftChild
                elif curr.value < val:
                    curr = curr.rightChild

            if curr.value == val:
                if not curr.leftChild and not curr.rightChild:
                    curr = None
                    return True
                elif curr.leftChild and not curr.rightChild:
                    curr = curr.leftChild
                    return True
                elif curr.rightChild and not curr.leftChild:
                    curr = curr.rightChild
                    return True
                else:
                    parent = curr
                    delNode = curr.rightChild
                    lefted = False
                    while delNode.leftChild:
                        lefted = True
                        parent = delNode
                        delNode = delNode.leftChild
                    curr.value = delNode.value

                    if lefted:
                        if delNode.rightChild:
                            parent.leftChild = delNode.rightChild
                        else:
                            parent.leftChild = None
                    else:
                        if delNode.rightChild:
                            parent.rightChild = delNode.rightChild
                        else:
                            parent.rightChild = None

        return False

    def rmvLowestChild(self):
        if self.root:
            self.root.rmvLowestChild()
        return False

    def getLowestChild(self):
        if self.root:
            return self.root.getLowestChild()
        return False

    def preorder(self):
        if self.root:
            print("PreOrder")
            return self.root.preorder()
        return False

    def postorder(self):
        if self.root:
            print("PostOrder")
            return self.root.postorder()
        return False

    def inorder(self):
        if self.root:
            print("InOrder")
            return self.root.inorder()
        return False

    def reversedOrder(self):
        if self.root:
            print("ReversedOrder")
            return self.root.reversedOrder()
        return False


bst = Tree()
bst.insert(10)
bst.insert(5)
bst.insert(4)
bst.insert(8)
bst.insert(6)
bst.insert(7)


bst.inorder()
bst.remove(5)



bst.inorder()
bst.insert(1)
bst.inorder()
