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
    Stack.push("월요일")
    Stack.push("화요일")
    Stack.push("수요일")
    Stack.push("목요일")
    Stack.push("목요일")
    Stack.push("금요일")
    Stack.push("토요일")
    Stack.pop()
    Stack.pop()
    Stack.pop()
    Stack.pop()
    Stack.pop()
    Stack.pop()
