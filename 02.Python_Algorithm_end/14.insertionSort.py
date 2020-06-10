def insertion_sort(sortData):
    for i in range(1, len(sortData)):
        key = sortData[i]
        #print(i, key)
        index = i - 1;
        for j in range(index, -1, -1):
            #print(j)
            if(sortData[j] > key):
                sortData[j + 1] = sortData[j]
                index -= 1
        #print("===========")
        #print(index)
        sortData[index + 1] = key
        print(sortData)

def insertion_sort2(sortData):
    for i in range(1, len(sortData)):
        j = i - 1
        key = sortData[i]		
        #while (sortData[j] < key) and (j >= 0):
        while sortData[j] < key and j >= 0:
            sortData[j + 1] = sortData[j]
            j = j - 1
        sortData[j + 1] = key
        print(sortData)

if __name__ == "__main__":
    #sortData = [19, 2, 31, 45, 30, 11, 121, 27]
    sortData = [8, 3, 4, 9, 1]
    insertion_sort(sortData)
    #print(sortData)
    print("============================")
    sortData = [8, 3, 4, 9, 1]
    insertion_sort2(sortData)
    #print(sortData)
