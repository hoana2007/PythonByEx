def linearsearch(A, key):
    position = 0
    flag = 0
    while position < len(A) and not flag:
        if A[position] == key: 
            flag = position
        else:
            position = position + 1
    return flag

A = [15, 86, 3, 21, 87]
key = 87
found = linearsearch(A,key)
print('Phan tu tim duoc o vi tri la: ', found)
print('do dai cua A: ', len(A))
