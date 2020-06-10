def soinsoo(number):
    sList = []
    n = number
    if n < 2:
        print("2보다 큰 숫자를 입력하세요")
        return
    while True:
        check = 2
        while True:
            r = n % check
            if r == 0:
                sList.append(check)
                break
            check += 1
        n = n // check
        #print(n, sList)
        if n == 1:
            break
    print("{} : {}".format(number, sList))

if __name__ == "__main__":
    number = int(input("소인수 분해할 숫자 : "))
    soinsoo(number)
