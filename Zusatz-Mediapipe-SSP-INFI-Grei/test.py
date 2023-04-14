from operator import ge
import cv2
import mediapipe as mp
import random
import json
from rec import get_gest

# ============================================ #
# TEAM - ZUSAMMENARBEIT: Fill, Steinlechner    #
# ============================================ #

# Parameter für Gestenerkennung die dann der methode get_gest mitgegeben werden

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


# Methoden die schon im bestehenden Programm von SWP bei Herr Rubner vorhanden waren

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
    
    
    
# Main-Methode - WICHTIG die Symbole Spock und Echse können nur vom Computer verwendet werden, da wir nur Gesten für Schere Stein und Papier einstudiert haben

if __name__ == '__main__':
    itemList = create_list()
    gameEnds = False
    print("Willkommen zum Schere Stein Papier Spiel")
    username = input("Wie lautet dein Username? ")
    user_data = get_user_data()
    
    while(gameEnds==False):
        input("Geben Sie mit Gesten Schere Stein Papier ein! - Wenn Sie bereit sind drücken Sie eine beliebige Taste: ")
        # Einlesen der Gesten
        itemP = get_gest(cap, hands, mpDraw, mpHands)
        # Game Ends (diese Funktion nicht möglich, da nur drei Gesten einstudiert)
        if itemP == 5:
            gameEnds=True
            break
        # Speicherung in Userfile (ebenfalls Funktion von SWP-Rubner)
        if username in user_data.keys():
            user_data[username][itemList[itemP]] +=1
        else:
            user_data[username] = {"Schere":0, "Papier":0, "Stein":0, "Echse": 0 , "Spock": 0, "Siege": 0, "Verloren": 0, "Unentschieden": 0}
            user_data[username][itemList[itemP]] = 1
        # Wahl von Computer 
        itemComp = comp()
        print(itemList[itemP])
        result_Comp_Win = check_computer_win(itemP, itemComp)
        # Gewonnen - nicht gewonnen
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
