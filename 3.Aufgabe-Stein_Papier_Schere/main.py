import keyboard
import random
import json


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

def get_user_data():
    file = open("data/user_data.txt", "r")
    
    return json.loads(file.read())

def save_user_data (dict):
    file = open("data/user_data.txt", "w")
    file.write(json.dumps(dict))
    file.close()




#TODO: Input-Handler

def checkConsoleInput(input):
    if(type(input) =="String"):
        if(input == "EXIT"):
            gameEnds = True
    pass

#TODO: Items as Enums
#TODO: Menue


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
            user_data[username] = {"Schere":0, "Papier":0, "Stein":0, "Echse": 0 , "Spock": 0, "Siege": 0, "Verloren": 0, "Unentschieden": 0}
            user_data[username][itemList[itemP]] = 1
        itemComp = comp()
        print(itemP)
        result_Comp_Win = check_computer_win(itemP, itemComp)
        if(result_Comp_Win):
            print("Der Computer hat gewonnen: "+itemList[itemComp]+" besiegt "+itemList[itemP])
            user_data[username]["Verloren"] +=1
        elif(itemP == itemComp):
            print("Unentschieden - ihr hattet beide: " + itemList[itemComp])
            user_data[username]["Unentschieden"] +=1
        else:
            user_data[username]["Siege"] +=1
            print("Der Computer zog " + itemList[itemComp])
            print("Gratulation - Du hast gewonnen!")
            
    save_user_data(user_data)    
    print("ENDE - Spielerstatistik:")   
    print("=========================")
    for user in user_data:
        print("Spieler " + user + ": " + str(user_data[user]))


        
        
            
