#========= SLL =======
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def size(self):
        cou = 0
        tmp = self.head
        while tmp is not None:
            cou = cou+1
            tmp = tmp.next
        return cou
    def addLast(self,value):
        p = Node(value)
        p.next = None
        if self.isEmpty():
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    def addFirst(self,value):
        p = Node(value)
        if self.isEmpty():
            self.head = self.tail = p
        else:
            p.next = self.head
            self.head = p
    def addMany(self,listValues):
        for k in listValues:
            self.addLast(k)
    def addPos(self, value, pos):
        if pos<1 or pos>self.size()+1:
            print('Out of range.')
            return -1
        p = Node(value)
        if self.isEmpty():
            self.head = self.tail = p
        else:
            if pos == 1:
                p.next = self.head
                self.head = p
            elif pos == self.size()+1:
                self.addLast(value)
            else:
                tmp = self.head
                i = 0
                while i < pos-1:
                    i = i+1
                    pre = tmp
                    tmp = tmp.next
                pre.next = p
                p.next = tmp
        return 0
    def removeFirst(self):
        if self.isEmpty():
            print('Nothing to remove.')
            return -1
        first_node = self.head
        self.head = self.head.next
        first_node = None
        return 0
    def removeLast(self):
        if self.isEmpty():
            print('Nothing to remove.')
            return -1
        elif self.size() == 1:
            self.head = self.tail = None
        else:
            tmp = self.head
            for k in range(1,self.size()-1):
                tmp = tmp.next
            self.tail = tmp
            self.tail.next = None
        return 0
    def removePos(self,pos):
        if pos<1 or pos>self.size():
            print('Out of range.')
            return -1
        elif pos == 1:
            self.removeFirst()
        elif pos == self.size():
            self.removeLast()
        else:
            k = 0
            tmp = self.head
            while k < pos-1:
                pre = tmp
                tmp = tmp.next
                k = k+1
            pre.next = tmp.next
            tmp = None
        return 0
    def removeAll(self):
        for k in range(1,self.size()+1):
            self.removeLast()
        print('Removed All.')
    def index(self,value):
        tmp = self.head
        for k in range(1,self.size()+1):
            if tmp.data == value:
                return k
            else:
                tmp = tmp.next
        if tmp == None:
            print('Can not found.')
            return -1
    def get(self,pos):
        tmp = self.head
        if pos<1 or pos>self.size():
            print('Out of range.')
            return
        for k in range(1,self.size()+1):
            if k == pos:
                return tmp
            else:
                tmp = tmp.next

    def printAll(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end = ' ')
            tmp = tmp.next

if __name__ == '__main__':
    sll = SLL()
    sll.addLast(2)
    sll.addFirst(3)
    sll.addMany([11,12,14])
    sll.addPos(100,3)
    print(sll.size())
    print(sll.index(11))
    print(sll.get(5))
    sll.removeFirst()
    sll.removeLast()
    sll.removePos(3)
    sll.removeAll()
    sll.printAll()