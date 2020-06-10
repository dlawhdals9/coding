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

Queue = Queue()
Queue.add("월요일")
Queue.add("화요일")
Queue.add("수요일")
Queue.add("목요일")
Queue.add("목요일")
Queue.add("금요일")
Queue.add("토요일")
Queue.remove()
Queue.remove()
Queue.remove()
Queue.remove()
Queue.remove()
Queue.remove()
Queue.add("일요일")
