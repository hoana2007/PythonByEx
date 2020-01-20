a = 50
b = 50
if a > b:
    print("a lon hon b")
elif a==b:
        print("a==b")
else: 
        print("b lon hon a")

if a > b: print("a lon hon b")

print(a) if a>b else print(b)

print(a) if a >  b else print(" = ") if a == b else print(b)