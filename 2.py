#2
n = int(input())
res = "NO"
for i in range (n):
    a = int(input())
    if a == 0:
        res = "YES"
print (res)
#вводим числа, делаем проверку есть ли среди них ноль или нет, если есть, пишем ЕС если нет,то НОУ