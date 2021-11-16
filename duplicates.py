list1 = [1,23,4,5,5,5,6,8,7,2,2,8,6,7,6,7]
result = []
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            result.append(list1[j])
print(list(set(result)))