class ArrayList():
    def __init__(self):
        self.ArrayList = [None] * 1
        self.size = 1

    def append(self, data):
        def append_wrap():
            for i in range(0, self.size):
                l = len(self)
                if self.ArrayList[i] == None:
                    self.ArrayList[i] = data
                    return True
            return False
        
        result = append_wrap()
        if result == False:
            self.ArrayList = self.ArrayList + ([None]*self.size)
            self.size *= 2
            self.append(data)
        return
    
    def remove_by_Index(self, index):
        def remove_wrap():
            self.ArrayList[index] = None
            if len(self) <= self.size/2:
                return False
            return True
        result = remove_wrap()
        if result == False:
            self.ArrayList = list(filter(lambda x: x != None, self.ArrayList))
            self.size /= 2
            
    def remove(self, data):
        def remove_wrap():
            for i in range(len(self)-1):
                if self.ArrayList[i] == data:
                    self.remove_by_Index(i)
            if len(self) <= self.size/2:
                return False
            return True
        result = remove_wrap()
        if result == False:
            self.ArrayList = list(filter(lambda x: x != None, self.ArrayList))
            self.size /= 2
                
    def __len__(self):
        l = 0
        for i in self.ArrayList:
            if i == None:
                pass
            else:
                l += 1
        return l

    def __str__(self):
        info = "["
        for i in self.ArrayList:
            if i != None:
                info += (str(i) + ",")
        info = (info[:-1] if len(info) > 1 else info) + "]"

        return info

