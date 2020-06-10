# https://wikidocs.net/book/1
class Stack:
    def __init__(self, size = 5):
        self.stack = [] # List 사용
        self.size = size
        self.top = 0

    def push(self, data):
        if data not in self.stack:
            if self.top < self.size:
                self.stack.append(data)
                self.top += 1
                print("스택에 {}을(를) PUSH합니다.".format(data))
            else:
                print("스택이 가득차서 {}을(를) PUSH할 수 없습니다.".format(data))
        else:
            print("{}은(는) 중복된 데이터입니다.".format(data))
        self.list()

    def pop(self):
        #if len(self.stack) <= 0:
        if self.top <= 0:
            print("스택에 저장된 데이터가 없습니다.")
        else:
            print("POP 데이터 :", self.stack.pop())
            self.top -= 1
            self.list()

    def list(self):
        print("===============================================")
        print("Stack에 저장된 데이터")
        if self.top <= 0:
            print("없음")
        else:
            for i in range(self.top):
                #print("스택에 저장된 {}번째 데이터 : {}".format(i + 1, self.stack[i]))
                if i > 0:
                    print(", ", end = "")
                print(self.stack[i], end = "")
            print()
        print("===============================================")
            
if __name__ == "__main__":
    Stack = Stack()
    menu = 0
    while True:
        while True:
            print("===============================")
            print(" 1.PUSH  2.POP  3.LIST  4.QUIT ")
            print("===============================")
            print("원하는 메뉴를 선택하세요 : ", end = "")
            menu = input()
            if menu >= "1" and menu <= "4":
                break
            print("메뉴를 다시 선택하세요")
        if menu == "1":
            data = input("스택에 저장할 데이터 : ")
            Stack.push(data)
        elif menu == "2":
            Stack.pop()
        elif menu == "3":
            Stack.list()
        elif menu == "4":
            break
    print("프로그램 종료")
