def factorial(number):
    sum = 1
    for i in range(1, number + 1):
        sum *= i
#    print("{} factorial = {}".format(number, sum))
    return sum

def factorialRecursion(number):
    if number == 1:
        return 1
    return number * factorialRecursion(number - 1)

if __name__ == "__main__":
    number = int(input("숫자 입력 : "))
    fact = factorial(number)
    print("{} factorial = {}".format(number, fact))
    print("==============================")
    fact = factorialRecursion(number)
    print("{} factorial = {}".format(number, fact))
    
