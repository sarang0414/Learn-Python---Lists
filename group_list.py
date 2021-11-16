def group(lists,n):
    result = []
    sub = []
    i = 0
    while i<len(lists):
        if len(sub)<n:
            sub.append(lists[i])
            i+=1
        else:
            result.append(sub)
            sub = []
    print(result)

group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
