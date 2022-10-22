class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.pre = None
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def size(self):
        tmp = self.head
        cou = 0
        while tmp is not None:
            cou = cou+1
            tmp = tmp.next
        return cou
    def printAll(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end = ' ')
            tmp = tmp.next
    def addFirst(self,value):
        p = Node(value)
        p.pre = None
        if self.isEmpty():
            self.head = self.tail = p
        else:
            self.head.pre = p
            p.next = self.head
            self.head = p
    def addLast(self,value):
        p = Node(value)
        p.next = None
        if self.isEmpty():
            self.head = self.tail = p
        else:
            p.pre = self.tail
            self.tail.next = p
            self.tail = p
    def addMany(self,listValues):
        for k in listValues:
            self.addLast(k)
    def addPos(self, value, pos):
        p = Node(value)
        if pos<1 or pos>self.size()+1:
            print('Out of range.')
            return -1
        if pos == 1:
            self.addFirst(value)
        elif pos == self.size()+1:
            self.addLast(value)
        else:
            tmp = self.head
            k = 1
            while k < pos:
                k = k+1
                pre = tmp
                tmp = tmp.next
            p.pre = pre
            p.next = tmp
            pre.next = p
            tmp.pre = p
        return 0

    def removeFirst(self):
        if self.isEmpty():
            print('Nothing to remove.')
            return -1
        pre = self.head
        if pre.next is not None:
            tmp = pre.next
            self.head = tmp
            pre = None
            tmp.pre = None
            return
        pre = None
        self.head = None
        return 0
    def removeLast(self):
        if self.isEmpty():
            print('Nothing to remove.')
            return -1
        tmp = self.tail
        pre = tmp.pre
        pre.next = None
        self.tail = pre
        tmp = None
        return 0
    def removePos(self,pos):
        if pos<1 or pos>self.size():
            print('Out of range.')
            return -1
        if pos == 1:
            self.removeFirst()
            return 0
        if pos == self.size():
            self.removeLast()
            return 0
        tmp = self.head
        k = 1
        while k < pos:
            k = k+1
            pre = tmp
            tmp = tmp.next
        aft = tmp.next
        pre.next = aft
        aft.pre = pre
        tmp = None
        return 0
    def removeAll(self):
        for k in range(1,self.size()+1):
            self.removeFirst()
    def index(self,value):
        tmp = self.head
        k = 1
        while k <= self.size():
            if tmp.data == value:
                return k
            tmp = tmp.next
            k = k+1
        if k == self.size()+1:
            print('Cannot found.')
            return -1
    def get(self,pos):
        if pos<1 or pos>self.size():
            print('Out of range.')
            return -1
        tmp = self.head
        k = 1
        while k <= self.size():
            if k == pos:
                return tmp.data
            tmp = tmp.next
            k = k+1
        return 0
    def printInfo(self):
        if self.isEmpty():
            print('List is empty.')
            return
        print('List: ',end = '')
        self.printAll()
        print('\nsize: ',self.size())
        print('Head: ',self.head.data,'; Pre Head: ',self.head.pre)
        print('Tail: ',self.tail.data,'; Next Tail: ',self.tail.next)
        print('=='*15)

if __name__ == '__main__':
    dll = DLL()
    dll.addLast(13)
    dll.addFirst(14)
    dll.addMany([21,22,23])
    dll.addPos(100,4)
    print(dll.index(101))
    print(dll.get(5))
    dll.removeFirst()
    dll.removeLast()
    dll.removePos(2)
    dll.removeAll()
    dll.printInfo()