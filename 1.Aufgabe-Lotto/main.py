import random

lottoStatistic={}
numbers = []
ziehung = []

def createLotto():
    numbers.clear()
    ziehung.clear()
    for i in range(45):
        numbers.append(i+1)

def createStatistics():
    global lottoStatistic
    for i in range(45):
        lottoStatistic[i+1] = 0

def getZiehung():
    limit=44
    for i in range(6):
        index = random.randint(0,limit)
        ziehung.append(numbers[index])
        numbers[index]= numbers[len(numbers)-1]
        del(numbers[len(numbers) - 1])
        limit-=1

    return ziehung

def getlottoStatistic(anz):
    for i in range(anz):
        nums = getZiehung()
        for j in nums:
            lottoStatistic[j] +=1
        createLotto()
    print(lottoStatistic)

if __name__ == "__main__":
    createLotto()
    createStatistics()
    getlottoStatistic(1000)