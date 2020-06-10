def euclid(a, b):
    max = a
    min = b
    if max < min:
        max, min = min, max
    #print("max : {}, min : {}".format(max, min))
    while True:
        r = max % min;
        if r == 0:
            break
        max = min
        min = r
    print("최대 공약수 : {}, 최소 공배수 : {}".format(min, int(a * b / min)))

if __name__ == "__main__":
    #a, b = input("숫자 두개 입력 : ").split()
    a, b = map(int, input("숫자 두개 입력 : ").split())
    #print(a + b)
    #a = int(a)
    #b = int(b)
    #print(a + b)
    euclid(a, b)
