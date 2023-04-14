
from prettytable import PrettyTable


#                 Single Linked List         Double Linked List          ArrayList
# isEmpty                 1                       1                       1
# _len_                   n                       n                       1
# getAllElements          n                       n                       n
# addElem                 n                       1                       1
# addAtIndex              n                       n                       n
# getFirstElem            1                       1                       1
# getLastElem             n                       1                       1
# deleteAllOcurrences     n                       n                       n
# contains                n                       n                       n
# indexOf                 n                       n                       n
# getItemAtIndex          n                       n                       1
# shuffle                 n                       n                       n




def printTable ():
    
    table = PrettyTable()
    table.field_names = ["Methoden","Einfach Verkettete Liste", "Doppelt Verkettete Liste", "unsere ArrayList"]
    table.add_row(["append","n","1","n"])
    table.add_row(["element_by_index","n","n","n"])
    table.add_row(["remove_by_index","n","n","n"])
    table.add_row(["remove_by_elem","n","n","n"])
    table.add_row(["len","n","n","n"])
    print(table)

