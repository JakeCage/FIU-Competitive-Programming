class Node:
    def __init__(self, data, next = None):
        self.value = data
        self.next = next

    def sortedList(self, aslist=[]):
        aslist.append(self.value)
        if self.next:
            return self.next.sortedList(aslist)
        return sorted(aslist)


    def sortedLinkedList(self):
        return LinkedList(self.sortedList())

    def get_next(self):
        return self.next

    def set_next(self, val):
        self.next = Node(val)
        return True

    def addToFront(self, val):
        if not self.next:
            self.next = Node(val)
            return True
        else:
            return self.next.addToFront(val)

    def findMedian(self, arr=[]):
        arr.append(self.value)

        if not self.next:
            if len(arr) % 2 == 0:
                return (arr[len(arr)//2 + arr[(len(arr)//2)+1]])/2
            return arr[len(arr)//2]
        else:
            return self.next.findMedian(arr)

    def addToBack(self, val):
        tmp = LinkedList(self.value)
        tmp.next = self.next
        self.next = tmp
        self.value = val
        return True

    def remove(self, val):
        if self.value == val:
            tmp = self.next.next
            self.value = self.next.value
            self.next = tmp
            return True
        else:
            return self.next.remove(val)

    def removeDuplicates(self, hashmap = {}):
        if self.value in hashmap:
            self.remove(self.value)
        else:
            hashmap[self.value] = True

        if self.next:
            return self.next.removeDuplicates()

        return True

    def find(self, val):
        if self.value:
            if self.value == val:
                return True
            if self.value != val:
                return self.next.find(val)
        else:
            return False

    def inorder(self):
        print(self.value)
        if self.next:
            return self.next.inorder()
        return True

    def makeCircular(self, root):
        if self.next:
            return self.next.makeCircular(root)
        self.next = root
        return True


#get set find remove
class LinkedList:
    def __init__(self, r=None):
        self.size = 0
        self.root = None
        if isinstance(r, list) and r:
            for num in r:
                self.addToFront(num)
        elif r:
            self.root = Node(r)
            self.size = 1

    def find(self, val):
        if self.root:
            return self.root.find(val)
        return False

    def inorder(self):
        if self.root:
            return self.root.inorder()
        return False

    def remove(self, val):
        if self.root:
            return self.root.remove(val)
        return False

    def findMedian(self):#without knowing the size
        if self.root:
            return self.root.findMedian()
        return False

    def removeDuplicates(self):
        if self.root:
            return self.root.removeDuplicates()
        return False

    def sortedLinkedList(self):
        if self.root:
            return self.root.sortedLinkedList()
        return False

    def get_next(self):
        if self.root:
            return self.root.get_next()
        return False

    def get_size(self):
        return self.size

    def addToFront(self, val):
        if self.root:
            self.size += 1
            return self.root.addToFront(val)
        else:
            self.root = Node(val)
            self.size += 1
            return True

    def addToBack(self, val):
        if self.root:
            self.size += 1
            return self.root.addToBack(val)
        else:
            self.root = Node(val)
            self.size += 1
            return True

    def sortedList(self):
        if self.root:
            return self.root.sortedList()
        return False

    def makeCircular(self):
        if self.root:
            self.root.makeCircular(self.root)


linked = LinkedList([4,3,3,2,8])
print(linked.findMedian())
# linked.inorder()
#
# print("-----")
#
# print("Size: " + str(linked.get_size()))
# linked = linked.sortedLinkedList()
# linked.inorder()
#
# print("-----")
#
# linked.removeDuplicates()
# print("Size: " + str(linked.get_size()))
# linked.inorder()
#
# print("-----")
# linked.makeCircular()
# linked.inorder()

