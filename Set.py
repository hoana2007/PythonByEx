my_set = {1,3}
print(my_set)

my_set.add(2)
print(my_set)

my_set.update([5,6,7,8])
print(my_set)

#xoa khoi set
my_set.discard(5)
print(my_set)

A = {1,2,3,4,5,6,7,8}
B = {2,9,8,6,4,3,4,5,6}

#Hop cua A,B
C = A|B

print(C)
print(A.union(B))

#print giao cua A,B

D = A&B
print(D)
print(A.intersection(B))

#hieu cua A-B
E = A-B
print(E)
print(A.difference(B))
print(B.difference(A))

#Bu cua A,B
print(A^B)
print(B^A)

#Kiem tra phan tu trong Set
print(10 in A)

#Tong A
print(sum(A))