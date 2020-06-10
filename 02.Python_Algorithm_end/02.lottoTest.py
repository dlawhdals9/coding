import random

def lotto(money):
    lotto = []
    for i in range(45):
        lotto.append(i + 1)
    '''
    for i in range(len(lotto)):
        print("{0:3d} ".format(lotto[i]), end = "")
        if (i + 1) % 10 == 0:
            print()
    print("\n================ 섞기전 ================")
    for i in range(1000000):
        r = random.randrange(1, 45, 1)
        lotto[0], lotto[r] = lotto[r], lotto[0]
    for i in range(len(lotto)):
        print("{0:3d} ".format(lotto[i]), end = "")
        if (i + 1) % 10 == 0:
            print()
    print("\n================ 섞은후 ================")
    '''
    for i in range(money // 1000):
        result = []
        for i in range(1000000):
            r = random.randrange(1, 45, 1)
            lotto[0], lotto[r] = lotto[r], lotto[0]
        print("1등 번호 : ", end = "")
        for i in range(6):
            #print("{0:3d} ".format(lotto[i]), end = "")
            result.append(lotto[i])
        result.sort()
        print(result)

if __name__ == "__main__":
    money = int(input("복권 구매 금액 : "));
    lotto(money)
    
