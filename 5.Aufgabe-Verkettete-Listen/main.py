import random
from linked_list import LinkedList

    # METHODS
    # ================
    # printlist +
    # is_empty +
    # __len__ +
    # add_at_index +
    # get_element_by_index +
    # append +
    # find (contain) ==> list1.find(30) ==>true/false +
    # get start +
    # get end +
    # get Index from element +
    # reverse +
    # remove all elements by object +
    # replace + 
    # add_first+
    # iter ==> durchiterieren
    # ================


def main():
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

if __name__ == '__main__':
    main()

    
