from classes import Gender, Person, Mitarbeiter, Abteilungsleiter, Firma, Abteilung


firma1 = Firma("Software-Solution")
leiter1 = Abteilungsleiter("Moni", Gender.WOMEN, firma1)
mitarbeiter1 = Mitarbeiter("Sylvia", Gender.WOMEN, firma1)
abteilung1 = Abteilung("Finanzabteilung", leiter1)
abteilung1.mitarbeiter.append(mitarbeiter1)

leiter2 = Abteilungsleiter("Maxl", Gender.MEN, firma1)
mitarbeiter2 = Mitarbeiter("Sylvia1", Gender.WOMEN, firma1)
abteilung2 = Abteilung("Finanzabteilung2", leiter2)
abteilung2.mitarbeiter.append(mitarbeiter1)
abteilung2.mitarbeiter.append(mitarbeiter2)

firma1.abteilungen.append(abteilung1)
firma1.abteilungen.append(abteilung2)

anz_women, anz_men = firma1.getPercentGender()

print("Anzahl Mitarbeiter in der Abteilung")
print(firma1.getAnzAbteilungen())

print("Anzahl Abteilungsleiter in der Firma")
print(firma1.getAnzAbteilungsleiter())

print("Anzahl der Abtielungen in der Firma")
print(firma1.getAnzAbteilungen())

print("Abteilung mit meisten Mitarbeiter")
print(firma1.getMaxAbteilung().name)

print("Prozentsätze - Geschlechter: ")
print("Männer: "+ str(anz_men) + " %")
print("Frauen: "+ str(anz_women) + " %")
print(abteilung1)
print(firma1)



