def perfectNumber(number):
    count = 0;
    for i in range(1, number + 1):
        sum = 0
        n = i // 2
        for j in range(1, n + 1):
            if i % j == 0:
                sum += j
        if i == sum:
            count += 1
            print("1에서 {}사이의 {}번째 완전수 {}".format(number, count, i))

if __name__ == "__main__":
    number = int(input("숫자 입력 : "))
    perfectNumber(number)
