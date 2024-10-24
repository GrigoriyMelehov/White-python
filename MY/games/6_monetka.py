import random
print('бросаем монетку 1000 раз')
input()
orel = 0
monetka = 0
while monetka<1000:
    if random.randint(0, 1) == 1:
        orel = orel + 1
    monetka = monetka + 1
    if monetka == 500:
        print(orel)
    if monetka == 300:
        print(orel)
    if monetka == 700:
        print(orel)
input()
print('Всего орлов за 1000 бросков')
print(orel)
