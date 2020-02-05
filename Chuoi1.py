a = 'hoana2007 %s %s' %('heng', 'heng 2')
print(a)

print('\n CHUỖI B: ')
b = '%s  %s'
result = b %(1,2)
print(result)
print(type(result))

c = '%d'
print(c %(3.6756754))

d = '%.2f'
print(d %(5.467342))

f = f'abcdeg'
print(f)
print(f' b\tb')

k = 'Kteam'
r_k = f'{k} - Education'
print(r_k)
print('\n')

name = 'Hòa'
address = 'Yên Lập town'
phone = '0944799986'
student_info = f'Họ và tên: {name}\nĐịa chỉ: {address}\nĐiện thoại: {phone}'
print(student_info)

#định dạng format
z = 'x:{3}, y:{1}, v:{0}, b: {2}'.format(1,2,3,4)
print(z)

q = 'thứ 1: {one}, thứ 2: {two}'.format(two = 333, one = 222)
print(q)

w = '{:-^10}'.format('heng')
print(w)