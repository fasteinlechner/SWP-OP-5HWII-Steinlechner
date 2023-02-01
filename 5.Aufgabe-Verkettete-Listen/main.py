import random

class ListElement:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        elem = self.head
        while elem is not None:
            yield elem
            elem = elem.next
    
    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count+=1
            current = current.next
        return count
    
    def is_empty(self):
        return self.head == None
    
    def print_list1(self):
        current = self.head
        while current is not None:
            print(current.data, end=", ")
            current = current.next
    
    def get_element_by_index (self, index):
        current = self.head
        for i in range (index):
            current = current.next
        return current
            
    def get_index_from_element(self, elem):
        index = 0
        current = self.head
        while current.data is not elem:
           current = current.next
           index+=1
        return index    
        
    def add_first(self, obj):
        obj = ListElement(obj)
        obj.next, self.head = self.head, obj
    
    def append(self,obj):
        obj = ListElement(obj)
        if self.head is None:
            self.head = obj
            return
        for current in self:
            pass
        current.next = obj
    def add_at_index(self, index, obj):
        obj = ListElement(obj)
        if index > len(self):
            print("INDEX out of range")
        current = self.head
        count = 0
        while current is not None:
            if count == index-1:
                current.next, obj.next = obj, current.next
                break
            current = current.next
            count +=1
                
    def find(self, obj):
        current = self.head
        while current is not None:
            if current.data is obj:
                return True
            else:
                current = current.next
        return False
    
    def remove_all_Elements_by_object(self, obj):
        element = self.head
        next = element.next
        
        if element.data == obj:
            self.head = self.head.next
        
        while next is not None:
            if next.data == obj:
                if next.next is not None:
                    while next.next.data == obj:
                        next = next.next
                    element.next = next.next
                else:
                    element.next = None
                    
            element = element.next
            if element == None:
                return
            next = element.next
             
              
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next, current.next = current.next, previous
            previous, current = current, next
            
        self.head = previous
        
    def replace(self, old, new):
        if old == new:
            return
        current = self.head
        while current is not None:
            if current.data == old:
                current.data = new
                return
            current = current.next
                
    def clear(self):
        self.head = None  
                  
    def get_start(self):
        return self.head.data
    
    def get_end(self):
        return self.get_element_by_index(len(self)-1).data
    
 
    # METHODS
    # ================
    # printlist +
    # is_empty +
    # __len__ +
    # add_at_index +
    # get_element_by_index +
    # append +
    # find ==> list1.find(30) ==>true/false +
    # get start +
    # get end +
    # get Index from element +
    # reverse +
    # remove all elements by object +
    # replace + 
    # add_first
    # ================
    

if __name__ == '__main__':
    list1 = LinkedList()
    print("LEERE Liste - Abfrage ob leer: ", list1.is_empty())
    for i in range(10):
        list1.append(random.randint(0,100))
    list1.print_list1()
    print()
    print("Liste befüllt - Abfrage ob leer: ", list1.is_empty())
    print("==================================================================================")
    print("Der Wert 50 wird hinzugefügt und an erster Stelle wird 0 hinzugefügt und an der Stelle 4 wird der Wert 5 eingefügt: ")
    list1.add_first(0)
    list1.append(50)
    list1.add_at_index(4, 5)
    list1.print_list1()
    print()
    print("Enthält die Liste die Zahl 0: ", list1.find(0))
    print("==================================================================================")
    print("Länge: ", len(list1))
    print("Element am Index 5: ", list1.get_element_by_index(5).data)
    print("Ende der Liste: ", list1.get_end())
    print("Index vom Wert 5: ", list1.get_index_from_element(5))
    print("Start der Liste: ", list1.get_start())
    list1.reverse() 
    list1.replace(50,10)
    print("==================================================================================")
    print("Liste mit REVERSE und REPLACE (50,10): ")
    list1.print_list1()
    print()
    print("Liste wird geleert:")
    list1.clear()
    print("Liste: ", list1.print_list1())

    
