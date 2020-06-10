def shellSort(sortData):
    #print(len(sortData))
    gap = len(sortData) // 2
    while gap > 0:
        for i in range(gap, len(sortData)):
            temp = sortData[i]
            j = i
            #print(gap, j, temp)
            while j >= gap and sortData[j - gap] > temp:
                sortData[j] = sortData[j - gap]
                j = j - gap
            sortData[j] = temp
        print("======================================")
        print(sortData)
        gap = gap // 2

if __name__ == "__main__":
    sortData = [19, 2, 31, 45, 30, 11, 121, 27]
    shellSort(sortData)
    #print(sortData)
