import random
def createLotto(anz):
    numbers.clear()
    for i in range(anz):
        numbers.append(i+1)

def createStatistics(anz):
    global lottoStatistic
    for i in range(anz):
        lottoStatistic[i+1] = 0

def getZiehung(anz):
    ziehung=[]
    limit=44
    for i in range(anz):
        index = random.randint(0,limit)
        ziehung.append(numbers[index])
        numbers[index]= numbers[len(numbers)-1]
        del(numbers[len(numbers) - 1])
        limit-=1
    return ziehung

def getlottoStatistic(anz, anzZiehung):
    for i in range(anz):
        nums = getZiehung(anzZiehung)
        for j in nums:
            lottoStatistic[j] +=1
        createLotto(45)
    print(sorted(lottoStatistic.values()))

# Ein guter Programmierer programmiert, das so, dass es dynamisch ist
#
if __name__ == "__main__":
    lottoStatistic = {}
    numbers = []
    createLotto(45)
    createStatistics(45)
    getlottoStatistic(100000, 6)