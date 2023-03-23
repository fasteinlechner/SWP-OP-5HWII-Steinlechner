class rechtecksForm:
    def __init__(self, bez):
        self.bezeichnung = bez

class dreiecksForm:
    def __init__(self, hoehe):
        self.hoehe = hoehe
        
    def printAttributes(self):
        print(self.hoehe)


class rechteck(rechtecksForm):
    def __init__(self, bez, laenge, breite):
        super().__init__(bez)
        self.laenge = laenge
        self.breite = breite
        
    def get_umfang(self):
        return 2*self.laenge + 2*self.breite


class quadrat(rechteck):
    def __init__(self, bez, laenge):
        super(rechteck, self).__init__(bez)
        self.laenge = laenge
    
    def get_umfang(self):
        return 4*self.laenge
        

class pyramid(rechtecksForm, dreiecksForm):
    def __init__(self, bez, hoehe):
        super().__init__(bez)
        self.hoehe = hoehe
        
    def printAttributes(self):
        return super().printAttributes()

        
        
        
if __name__ == "__main__":
    r1 = rechteck("r1", 10, 5)
    print("Umfang Rechteck (10,5): ", r1.get_umfang())
    q1 = quadrat("q1", 10)
    print("Umfang Quadrat (10): ", q1.get_umfang())
    
    p1 = pyramid("p1", 10)
    print("Bezeichnung: ", p1.bezeichnung)
    print("Höhe: ", p1.hoehe)
    p1.printAttributes()
    


 
