from random import random
import random

def get_median(items):
    n= len(items)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if items[j] > items[j+1]:
                swapped = True
                items[j], items[j+1] = items[j+1], items[j]
        if not swapped:
            break
    print(items)
    median_index = (len(items)-1)//2
    return items[median_index]

def get_average(items):
    sum = 0
    for i in items:
        sum +=i
    return sum/len(items)

if __name__ == '__main__':
    item_list = []
    for i in range(11):
        item_list.append(random.randint(0, 10)) 
    print(item_list)
    
    median = get_median(item_list)
    average = get_average(item_list)
    
    
    print("Median: ", median)
    print("Average: ", average)