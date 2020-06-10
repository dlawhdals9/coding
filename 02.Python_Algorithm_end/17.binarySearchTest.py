def sort(data):
    for i in range(len(data) - 1):
        #print(i)
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
        print(data)

def binarySearch(data, number):
    count = 0
    start = 0
    end = len(data) - 1
    middle = 0
    flag = False
    while start <= end:
        middle = (start + end) // 2
        count += 1
        print("start : {}, end : {}, middle : {}".format(start, end, middle))
        if data[middle] > number:
            end = middle - 1
        elif data[middle] < number:
            start = middle + 1
        else:
            flag = True
            break
    print("{}번 비교".format(count))
    if flag:
        print("검색 성공!!! {}는 {}번째 데이터 입니다.".format(number, middle))
    else:
        print("검색 실패!!! {}는 존재하지 않는 데이터 입니다.".format(number))

if __name__ == "__main__":
    data = [19, 2, 31, 45, 30, 11, 121, 27]
    sort(data)
    number = int(input("검색할 데이터 : "))
    binarySearch(data, number)
    
