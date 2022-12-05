from enum import Enum

class Gender(Enum):
    MEN = 0
    WOMEN = 1

class Person():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Mitarbeiter(Person):
    def __init__(self, name, gender, firma):
        super().__init__(name, gender)
        self.firma = firma

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, firma):
        super().__init__(name, gender, firma)

class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []
        
    def getAnzMitarbeiter(self):
        anzahl = 0
        for abteilung in self.abteilungen:
            anzahl += len(abteilung.mitarbeiter)
        return anzahl
            
    def getAnzAbteilungsleiter(self):
        anzahl = 0
        for abteilung in self.abteilungen:
            anzahl += len(abteilung.abteilungsleiter)
        return anzahl
    
    def getAnzAbteilungen(self):
        return len(self.abteilungen)
    
    def getMaxAbteilung(self):
        maxAbteilung = self.abteilungen[0]
        for abteilung in self.abteilungen:
            if len(abteilung.mitarbeiter) > len(maxAbteilung.mitarbeiter):
                maxAbteilung = abteilung;
        return maxAbteilung
    
    def getPercentGender(self):
        anz_men = 0
        anz_women = 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.gender == Gender.WOMEN:
                    anz_women +=1
                else:
                    anz_men +=1
            for abteilungsleiter in abteilung.abteilungsleiter:
                if abteilungsleiter.gender == Gender.WOMEN:
                    anz_women +=1
                else: 
                    anz_men +=1
        return (anz_women/(anz_men+anz_women))*100, (anz_men/(anz_men+anz_women))*100

class Abteilung():
    def __init__(self, name, abteilungsleiter):
        self.name = name
        self.abteilungsleiter = []
        self.abteilungsleiter.append(abteilungsleiter)
        self.mitarbeiter = []
    

    