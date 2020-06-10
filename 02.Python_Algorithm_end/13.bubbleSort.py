def bubble_sort(sortData):
    for i in range(len(sortData) - 1):
        for j in range(len(sortData) - i - 1):
            #print("i = {}, j = {}".format(i, j))
            if sortData[j] > sortData[j + 1]:
                sortData[j], sortData[j + 1] = sortData[j + 1], sortData[j]
        print(sortData)    

def bubble_sort2(sortData):
    for i in range(len(sortData) - 1):
        flag = True
        for j in range(len(sortData) - i - 1):
            if sortData[j] < sortData[j + 1]:
                sortData[j], sortData[j + 1] = sortData[j + 1], sortData[j]
                flag = False
        if flag == True:
            break
        print(sortData)

if __name__ == "__main__":
    sortData = [8, 3, 4, 9, 1]
    bubble_sort(sortData)
    #print(sortData)
    print("=====================================")
    sortData = [1, 9, 8, 4, 3]
    bubble_sort(sortData)
    #print(sortData)
    print("=====================================")
    sortData = [1, 9, 8, 4, 3]
    bubble_sort2(sortData)
    #print(sortData)
