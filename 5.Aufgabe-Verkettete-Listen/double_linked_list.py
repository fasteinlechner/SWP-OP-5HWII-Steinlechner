import math
import random

class ListElement:
    def __init__(self, objData = None, next=None, prev=None): 
        self.objData = objData
        self.next = next
        self.previous = prev

    def __str__(self):
        return str(self.objData)

class DoubleLinkedList():
    def __init__(self):  
        self.head = None
        self.tail = None
  
    def append(self, data):
        newElem = ListElement(data)
        if self.head == None:
            self.head = newElem
            self.tail = newElem
        elif self.head.next == None:
            self.tail = newElem
            self.head.next = self.tail
            self.tail.previous = self.head
        else:
            temp = self.tail
            self.tail = newElem
            self.tail.previous = temp
            self.tail.previous.next = newElem
        
    def remove(self, elem=None):
        if elem == None:
            self.tail = self.tail.previous
            self.tail.previous.next = self.tail
            self.tail.next = None
        else:
            elemToDelete = self.elemAtIndex(self.index(elem))
            if elemToDelete.next == None:
                self.tail = self.tail.previous
                self.tail.previous.next = self.tail
                self.tail.next = None
            else:
                elemToDelete = elemToDelete.previous
                elemToDelete.next = elemToDelete.next.next

    def removePos(self, index):
        self.remove(self[index])
        
    def __len__(self):
        count = 0
        nextElem = self.head
        while not nextElem == None:
            nextElem = nextElem.next
            count += 1
        return count
    
    def index(self, elem):
        i = 0
        temp = self.head
        while not temp == elem:
            if temp == None:
                return
            temp = temp.next
            i += 1
        return i
    
    def getItems(self, a, b):
        items = DoubleLinkedList()
        if a >= len(self):
            return None
        if b >= len(self):
            b = len(self)
        if a == b or a+1 == b:
            return self[a] if self[a] != None else None
        for i in range(int(a), int(b)):
            items.append(self[i])
        return items
    
    def bubble_sort(self):
        n = len(self)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self[j] > self[j+1]:
                    swapped = True
                    self[j], self[j+1] = self[j+1], self[j]
                                       

    def __getitem__(self, index):
        e = self.head
        while not self.index(e) == index:
            e = e.next
            if e == None:
                return None
        return e.objData
    
    def __setitem__(self, index, val):
        e = self.head
        if index == -1:
            return e
        while not self.index(e) == index:
            if e == None:
                break
            e = e.next
        e.objData = val
                    
    def split(self, parts):
        l = len(self)
        p = parts
        if parts > l:
            print("List only has ", l, " So you cant split it:) Error:100234")
            return
        splitLists = List()
        for i in range(parts):
            elemForPart = int(l/p)
            listPart = List()
            for j in range(len(self)-l,len(self)-l+elemForPart):
                listPart.append(self[j])
            splitLists.append(listPart)
            p -= 1
            l -= elemForPart
        return splitLists  
    
    def shuffleList(self):
        for i in range(len(self)):
            rand = random.randint(0, len(self)-1)
            currPos = self[i]
            randPos = self[rand]
            self[i] = randPos
            self[rand] = currPos
        return self

    def getData(self):
        current = self.head
        info = "["
        while(current):
            if type(current.objData) == List:
                info += current.objData.getData() + ","
            else:
                info += str(current.objData) + ","
            current = current.next
        info = info[:-1] + "]"
        return info

    def __str__(self):
        current = self.head
        info = "["
        while(current):
            if type(current.objData) == List:
                info += current.objData.getData() + ","
            else:
                info += str(current.objData) + ","
            current = current.next
        info = info[:-1] + "]"
        return info