def selection_sort(sortData):
    for i in range(len(sortData) - 1):
        #print(i)
        for j in range(i + 1, len(sortData)):
            if sortData[i] > sortData[j]:
                imsi = sortData[i]
                sortData[i] = sortData[j]
                sortData[j] = imsi
                #sortData[i], sortData[j] = sortData[j], sortData[i]
        print(sortData)

def selection_sort2(sortData):
    for i in range(len(sortData) - 1):
        min_i = i
        for j in range(i + 1, len(sortData)):
            if sortData[min_i] < sortData[j]:
                min_i = j
        sortData[i], sortData[min_i] = sortData[min_i], sortData[i]

if __name__ == "__main__":
    sortData = [8, 3, 4, 9, 1]
    selection_sort(sortData)
    #print(sortData)
    print("=====================================")
    sortData = [8, 3, 4, 9, 1]
    selection_sort2(sortData)
    print(sortData)
