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


