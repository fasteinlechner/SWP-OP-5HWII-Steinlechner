import random

def generate_cards(anz):
    cards = []
    for i in range (anz):
        card = random.randint(0,51)
        while card in cards:
            card = random.randint(0,51)
        cards.append(card)
    return cards

def generate_dict():
    statistics = {"RoyalFlush":0, "Straight Flush":0, "Four of a Kind":0, "Full House":0, "Flush":0, "Straight":0, "Three of a Kind": 0, "Two Pair":0, "One Pair":0, "High Card":0}
    return statistics

def get_color (list):
    colors =[]
    for i in list:
        colors.append(i//13)
    return colors

def get_types(list):
    types = []
    for i in list:
        types.append(i%13)
    return types

def determine_combi (statistics, colors, types):
    #Ermittlung der "höchsten" Farbe bzw. Symbols
    color_max = colors.count(max(colors, key = colors.count))
    type_max = types.count(max(types, key=types.count))
    
    if color_max == 5:
        if list(range(8,13)) == types:
            statistics["Royal Flush"] +=1
            return
        types.sort()
        if types[-1] -4 == types[0]:
            statistics["Straight Flush"] +=1
            return
        statistics["Flush"] +=1
        return
    if type_max >=2:
        if type_max >=3:
            if type_max ==4:
                statistics["Four of a Kind"]+=1
                return
            else:
                full_house_list = [x for x in types if x != max(types, key=types.count)]
                if full_house_list.count(max(full_house_list, key=full_house_list.count)) == 2:
                    statistics["Full House"]+=1
                    return
                statistics["Three of a Kind"]+=1
                return
        else:
            two_pair_list = [x for x in types if x != max(types, key= types.count)]
            if two_pair_list.count(max(two_pair_list, key=two_pair_list.count)) == 2:
                statistics["Two Pair"]+=1
                return
            statistics["One Pair"]+=1
            return
    types.sort()
    if types[-1] -4 == types[0]:
        statistics["Straight"]+=1
        return
    statistics["High Card"]+=1
    return
        
    
            
    

if __name__ == '__main__':
    stat = generate_dict()
    anz = 100000
    for i in range(anz):
        cards = generate_cards(5)
        determine_combi(stat, get_color(cards), get_types(cards))
    print("*************RESULT*************")
    print("================================")
    print(stat)
    print("***********COMPARISON***********")
    print("================================")
    act_perc = []
    avg_perc = [0.00015, 0.0013, 0.021, 0.143, 0.20, 0.391, 2.112, 4.81, 42.25, 50.21]
    for i in stat.values():
        act_perc.append(i/anz*100)
    print("AkTUELLE ZIEHUNG:")
    print(act_perc)
    print("DURCHSCHNITTLICHE ZIEHUNG:")
    print(avg_perc)
        
    
        
        


