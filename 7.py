#7
a = int(input())
d = 2
# d = 2, т.к. само число и 1
for i in range(2, int(a/2) + 1):
# собственно, в промежутке между двумя и заданном числе, деленном на два.
# int чтобы были целые числа.
    if a % i == 0:
        d += 1
print(d)