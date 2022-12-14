import random

def get_order_descending(items):
    n = len(items)
    for i in range(n-1):
        for j in range(n-i-1):
            if items[j] < items[j+1]:
                items[j], items[j+1] = items[j+1], items[j] 
    return items

def get_quantil(items):
    n = len(items)
    items = get_order_descending(items)
    quantile_index = ((n)//4)
    quantile_items = []
    for i in range(0, quantile_index):
        quantile_items.append(items[i])
    return quantile_items

if __name__ == "__main__":
    list_item = []
    for i in range(4):
        list_item.append(random.randint(0,10))
    print(list_item)
    des_list = get_order_descending(list_item)
    quantile = get_quantil(list_item)
    
    print("Descending: ",des_list)
    print("Quantil: ", quantile)
    