def lensort(lists):
    lists.sort(key=lambda x:len(x))
    data = sorted(lists,key=lambda x:len(x))
    print(lists)
    print(data)

lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
