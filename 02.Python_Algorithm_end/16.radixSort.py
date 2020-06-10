def radix_sort(sortData):
    is_sorted = False
    position = 1
 
    while not is_sorted:
        is_sorted = True
        queue_list = [list() for i in range(10)]
 
        for num in sortData:
            digit_number = (int)(num / position) % 10
            queue_list[digit_number].append(num)
            if is_sorted and digit_number > 0:
                is_sorted = False

        index = 0
        for numbers in queue_list:
            for num in numbers:
                sortData[index] = num
                index += 1

        print(sortData)
 
        position *= 10

if __name__ == "__main__":
    sortData = [19, 2, 31, 45, 30, 11, 121, 27]
    radix_sort(sortData)
    #print(sortData)
