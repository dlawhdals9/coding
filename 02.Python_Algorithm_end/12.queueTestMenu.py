class Queue:
    def __init__(self, size = 5):
        self.queue = list()
        self.size = size
        self.front = 0
        self.rear = 0

    def add(self, data):
        if data not in self.queue:  
            if self.rear < self.size:
                self.queue.append(data)
                self.rear += 1
                print("큐에 {}을(를) 입력합니다.".format(data))
            else:
                print("큐가 가득차서 {}을(를) 입력할 수 없습니다.".format(data))
        else:
            print("{}은(는) 중복된 데이터입니다.".format(data))
        self.list()  

    def remove(self):
        if self.rear == 0 or self.rear == self.front:
            print("큐에 저장된 데이터가 없습니다.")
        else:
            print("출력된 데이터 :", self.queue[self.front])
            self.queue[self.front] = ""
            self.front += 1
            self.list()

    def list(self):
        print("===============================================")
        print("Queue에 저장된 데이터")
        if self.rear == 0 or self.rear == self.front:
            print("없음")
        else:
            for i in range(0, len(self.queue)):
                #print("큐에 저장된 {}번째 데이터 : {}".format(i + 1, self.queue[i]))
                if i > self.front:
                    print(", ", end = "")
                print(self.queue[i], end = "")
            print()
        print("===============================================")

if __name__ == "__main__":
    Queue = Queue()
    menu = 0
    while True:
        while True:
            print("====================================")
            print(" 1.입력  2.출력  3.목록보기  4.종료 ")
            print("====================================")
            print("원하는 메뉴를 선택하세요 : ", end = "")
            menu = input()
            if menu >= "1" and menu <= "4":
                break
            print("메뉴를 다시 선택하세요")
        if menu == "1":
            data = input("큐에 저장할 데이터 : ")
            Queue.add(data)
        elif menu == "2":
            Queue.remove()
        elif menu == "3":
            Queue.list()
        elif menu == "4":
            break
    print("프로그램 종료")

