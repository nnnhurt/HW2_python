p = int(input())
c = 0
d = int(input())
for i in range(p):
    if c == 0:
        c = d
    else:
        if c > 0:
            if c > d:
                c += d
            else:
                c = d
print(c)

