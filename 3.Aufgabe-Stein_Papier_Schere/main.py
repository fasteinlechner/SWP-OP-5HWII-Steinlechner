import keyboard
import random


def get_user_data():
    user_data = {"steini": {"Schere":0, "Papier":0, "Stein":0, "Echse": 0 , "Spock": 0, "Siege":3}}
    
    return user_data

def create_list():
    itemList = ['Schere', 'Papier', 'Stein', 'Echse', 'Spock' ] 
    return itemList;

def comp():
    return random.randint(0,4)

def check_computer_win(player, computer):
    result = False
    print(player)
    if computer == (player+2)%5 or computer == (player-1)%5:
        result = True
    return result


#TODO: Input-Handler
#TODO: Items as Enums
#TODO: Save Data



# Main-Methode
if __name__ == '__main__':
    itemList = create_list()
    gameEnds = False
    print("Willkommen zum Schere Stein Papier Echse Spock Spiel")
    username = input("Wie lautet dein Username? ")
    user_data = get_user_data()
    while(gameEnds==False):
        itemP = int(input("Wählen Sie Schere [0] Papier [1] Stein [2] Echse [3] Spock[4]! "))
        if itemP == 5:
            gameEnds=True
            break
        if username in user_data.keys():
            user_data[username][itemList[itemP]] +=1
        else:
            user_data[username] = {"Schere":0, "Papier":0, "Stein":0, "Echse": 0 , "Spock": 0, "Siege":0}
            user_data[username][itemList[itemP]] = 1
        itemComp = comp()
        print(itemP)
        result_Comp_Win = check_computer_win(itemP, itemComp)
        if(result_Comp_Win):
            print("Der Computer hat gewonnen: "+itemList[itemComp]+" besiegt "+itemList[itemP])
        elif(itemP == itemComp):
            print("Unentschieden - ihr hattet beide: " + itemList[itemComp])
        else:
            print("Der Computer zog " + itemList[itemComp])
            print("Gratulation - Du hast gewonnen!")
        
    print("ENDE - Spielerstatistik:")    
    print("=========================")
    for user in user_data:
        print("Spieler " + user + ": " + str(user_data[user]))

        
        
            
