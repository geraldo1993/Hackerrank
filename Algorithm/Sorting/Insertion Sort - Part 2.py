def insertionSort(ar):
    length = len(ar)
    condtion  = False
    count = 1
    while not False:
        start = ar[count]
        for i in range(count - 1, -1, -1):
            if start < ar[i]:
                ar[i + 1], ar[i] = ar[i], start
        print " ".join(map(str, ar))
        count+= 1
        if count == length:
            condition = True
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
