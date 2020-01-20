try:
    f = open("file1.txt", encoding='utf-8')
    a = f.readline()
    b = f.readline()
    tg = int(a)+int(b)
    print(tg)
    f1 = open("file2.txt",'w')
    for i in range(20):
       f1.write("This is line %d \r\n" % (i+1))
finally:
    f.close()
    f1.close()

import os
print(os.listdir())



