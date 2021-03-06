# LinkedList에 저장할 데이터를 기억하는 클래스
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

# LinkedList 자체를 의미하는 클래스
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0;

    # 맨 앞에 데이터를 추가하는 메소드
    def appendFirst(self, data):
        self.count += 1
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # 맨 뒤에 데이터를 추가하는 메소드
    def appendLast(self, data):
        self.count += 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newNode

    # 지정한 위치 다음에 데이터를 추가하는 메소드
    def appendbetween(self, position, data):
        if position < 1 or position > self.count:
            print("데이터를 추가할 위치가 잘못되었습니다.")
            return
        self.count += 1
        node = self.head
        newNode = Node(data)
        for i in range(position - 1):
            node = node.next
        #print(node.data)
        newNode.next = node.next
        node.next = newNode

    # 지정된 데이터를 삭제하는 메소드
    def remove(self, data):
        node = self.head
        if (node is not None):
            #print("LinkedList가 비어있지 않습니다.")
            #print(node.data)
            #print(data)
            if(node.data == data):
                self.head = node.next
                self.count -= 1
                return
            while (node is not None):
                if node.data == data:
                    break
                prev = node
                node = node.next
            if(node == None):
                print("LinkedList에 삭제할 데이터가 없습니다.")
                return
            prev.next = node.next
            self.count -= 1
        else:
            print("LinkedList가 비어있습니다.")

    # 저장된 모든 데이터를 출력하는 메소드
    def listPrint(self):
        node = self.head
        if node:
            print(self.count, "개의 데이터가 LinkedList에 저장되어 있습니다.")
            #while node is not None:
            for i in range(self.count - 1):
                print(node.data, end = " ")
                node = node.next
            print(node.data)
        else:
            print("LinkedList에 저장된 데이터가 없습니다.")

    # 특정 위치의 데이터를 검색하는 메소드
    def search(self, position):
        if position < 1 or position > self.count:
            print("데이터를 검색할 위치가 잘못되었습니다.")
            return
        node = self.head
        for i in range(position - 1):
            node = node.next
        #print(position, "번째 데이터는", node.data, "입니다.")
        #print("%d 번째 데이터는 %s 입니다." % (position, node.data))
        print("{} 번째 데이터는 {} 입니다.".format(position, node.data))

    # 특정 데이터를 검색해서 출현하는 위치를 출력하는 메소드
    def searchItem(self, data):
        count = 0;
        node = self.head
        for i in range(self.count):
            if node.data == data:
                count += 1
                print("{}는 {}번째 위치에 있는 데이터 입니다.".format(data, i))
            node = node.next
        if(count == 0):
            print("{}를 찾을 수 없습니다.".format(data))
        
if __name__ == "__main__":
    # LinkedList를 만든다.
    print("================================================")
    list = LinkedList()
    list.listPrint()
    print("================================================")
    # 데이터를 LinkedList 맨 뒤에 추가한다.
    #'''
    list.appendLast("월요일")
    list.listPrint()
    print("================================================")
    list.appendLast("화요일")
    list.appendLast("목요일")
    list.appendLast("금요일")
    list.appendLast("토요일")
    list.listPrint()
    print("================================================")
    # 데이터를 LinkedList 맨 앞에 추가한다.
    list.appendFirst("일요일")
    list.listPrint()
    print("================================================")
    # 데이터를 LinkedList의 지정된 위치 다음에 추가한다.
    list.appendbetween(3, "수요일")
    list.listPrint()
    print("================================================")
    #'''
    # 데이터를 제거한다.
    list.remove("수요일")
    list.listPrint()
    print("================================================")
    # 특정 위치의 데이터를 검색한다.
    list.search(6)
    print("================================================")
    list.appendLast("일요일")
    list.appendLast("일요일")
    list.listPrint()
    # 특정 데이터의 위치를 검색한다.
    list.searchItem("일요일")
    print("================================================")
