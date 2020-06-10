def decTobin(dec):
    number = dec
    convert = []
    while True:
        mok = dec // 2
        nmg = dec % 2
        convert.insert(0, nmg)
        if mok == 0:
            break
        dec = mok
    #print("{} : {}".format(number, convert))
    print("{} : ".format(number), end = "")
    for i in range(len(convert)):
        print(convert[i], end = " ")
    print()

def decTooct(dec):
    number = dec
    convert = []
    while True:
        mok = dec // 8
        nmg = dec % 8
        convert.insert(0, nmg)
        if mok == 0:
            break
        dec = mok
    #print("{} : {}".format(number, convert))
    print("{} : ".format(number), end = "")
    for i in range(len(convert)):
        print(convert[i], end = " ")
    print()

def decTohex(dec):
    number = dec
    convert = []
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    while True:
        mok = dec // 16
        nmg = dec % 16
        convert.insert(0, hex[nmg])
        if mok == 0:
            break
        dec = mok
    #print("{} : {}".format(number, convert))
    print("{} : ".format(number), end = "")
    for i in range(len(convert)):
        print(convert[i], end = " ")
    print()

if __name__ == "__main__":
    dec = int(input("10진수 입력 : "))
    decTobin(dec)
    decTooct(dec)
    decTohex(dec)
