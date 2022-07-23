# 双方向リストを利用

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def push(self,val):
        newNode = Node(val)
        if (not self.head):
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        self.length = self.length + 1
        return self
    
    def pop(self):
        if(not self.head):
            return None

        currentTail = self.tail
        if (self.length == 1):
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            currentTail.prev = None

        self.length = self.length - 1
        return currentTail
    
    def shift(self):
        if (self.length == 0):
            return None
        oldHead = self.head
        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = oldHead.next

        self.length = self.length - 1
        return oldHead

    def unshift(self, val):
        newNode = Node(val)
        if (self.length == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length = self.length + 1
        return self
    
    def get(self, index):
        if ((index < 0) or (index > self.length)):
            return None

        halfOfLength = self.length // 2
        if (index <= halfOfLength):
            counter = 0
            current = self.head
            while(counter != index):
                current = current.next
                counter = counter + 1
            return current
        elif (index > halfOfLength):
            counter = self.length - 1
            current = self.tail
            while(counter != index):
                current = current.prev
                counter = counter - 1
            return current

    def set(self, index, val):
        targetNode = self.get(index)
        if(targetNode):
            targetNode.val = val
            return True
        else:
            return False

    def insert(self, index, val):
        if((index < 0) or (index > self.length)):
            return False
        if (index == 0):
            self.unshift(val)
        if (index == self.length):
            self.push(val)
        prevNode = self.get(index - 1)
        newNode = Node(val)
        nextNode = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        nextNode.prev = newNode
        newNode.next = nextNode
        self.length = self.length + 1

        return True

    def remove(self, index):
        if((index < 0) or (index >= self.length)):
            return None
        if (index == 0):
            self.shift()
        if (index == self.length - 1):
            self.pop()
        removedNode = self.get(index)
        removedNode.prev.next = removedNode.next
        removedNode.next.prev = removedNode.prev
        removedNode.next = None
        removedNode.prev = None

        self.length = self.length - 1
        return removedNode
    
    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node

        tmpPrev = None
        tmpNext = None
        while(node):
            tmpPrev = node.prev
            tmpNext = node.next
            node.next = tmpPrev
            node.prev = tmpNext
            node = node.prev

        return self
