class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class CLL:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def rotate(self,number):
        if number == 0:
            return -1
        if number >= self.size():
            return -1
        tmp = self.head
        for i in range(1,self.size()-number):
            tmp = tmp.next
        self.head = tmp.next
        return 0
    def size(self):
        tmp = self.head
        cou = 0
        while tmp is not None:
            cou = cou+1
            tmp = tmp.next
            if tmp == self.head:
                break
        return cou
    def addLast(self,value):
        p = Node(value)
        if self.isEmpty():
            self.head = p
            p.next = p
        else:
            p.next = self.head
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            tmp.next = p
    def addFirst(self,value):
        p = Node(value)
        if self.isEmpty():
            self.head = p
            p.next = p
        else:
            p.next = self.head
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            tmp.next = p
            self.head = p

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
                pre = tmp
                k = k + 1
                tmp = tmp.next
            pre.next = p
            p.next = tmp
        return 0

    def removeFirst(self):
        if self.isEmpty():
            print('Nothing to remove.')
            return -1
        if self.size() == 1:
            self.head.next = None
            self.head = None
            return 0
        tmp = self.head
        while tmp.next != self.head:
            tmp = tmp.next
        tmp.next = self.head.next
        pre = self.head
        self.head = tmp.next
        pre = None
        return 0

    def removeLast(self):
        if self.isEmpty():
            print('Nothing to remove.')
            return -1
        if self.size() == 1:
            self.head = None
            return 0
        tmp = self.head
        while tmp.next != self.head:
            pre = tmp
            tmp = tmp.next
        pre.next = self.head
        tmp = None
        return 0
    def removePos(self,pos):
        if pos<1 or pos> self.size():
            print('Out of range.')
            return -1
        if self.isEmpty():
            print('Nothing to remove.')
            return -1
        if pos == 1:
            self.removeFirst()
            return 0
        elif pos == self.size():
            self.removeLast()
            return 0
        tmp = self.head
        k = 1
        while k < pos:
            k = k+1
            pre = tmp
            tmp = tmp.next
        pre.next = tmp.next
        tmp = None
        return 0
    def removeAll(self):
        for i in range(1,self.size()+1):
            self.removeFirst()

    def index(self,value):
        if self.isEmpty():
            print('CLL is empty.')
            return -1
        k = 1
        tmp = self.head
        while k < self.size()+1:
            if tmp.data == value:
                return k
            tmp = tmp.next
            k = k+1
        if k == self.size()+1:
            print('Cannot found.')
            return -1
    def get(self,pos):
        if pos <1 or pos> self.size():
            print('Out of range.')
            return
        tmp = self.head
        for k in range(1,self.size()+1):
            if k == pos:
                return tmp.data
            tmp = tmp.next

    def printAll(self):
        if self.size() == 0:
            print('Empty.')
            return
        tmp = self.head
        while True:
            print(tmp.data, end = ' ')
            tmp = tmp.next
            if tmp == self.head:
                break
if __name__ == '__main__':
    cll = CLL()
    cll.addLast(10)
    cll.addPos(100,3)
    cll.addFirst(15)
    cll.rotate(2)
    print(cll.index(10))
    print(cll.get(3))
    cll.removePos(4)
    cll.removeFirst()
    cll.removeLast()
    cll.removeAll()
    cll.printAll()