import random
import time
import os

def GamePole(): #генерация значений игрового поля
    Pole = []
    for i in range(0,9):
        L = random.randint(0, 3)
        if L == 0:
            Pole = Pole + ['O']
        if L == 1:
            Pole = Pole + ['X']
        if L == 2:
            Pole = Pole + ['Z']
        else:
            Pole = Pole + ['Y']
    return Pole

def Game(Pole, Bet, PolePer): #расчет выигрыша по ставке
    i = 0
    u = 0
    if (Pole[0] == Pole[1] == Pole[2] == PolePer[0] or Pole[0] == Pole[1] == Pole[2] == PolePer[1] or Pole[0] == Pole[1] == Pole[2] == PolePer[2]):
        TheBet = 5* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE2= ' + str(TheBet))
    if (Pole[3] == Pole[4] == Pole[5] == PolePer[0] or Pole[3] == Pole[4] == Pole[5] == PolePer[1] or Pole[3] == Pole[4] == Pole[5] == PolePer[2]):
        TheBet = 5* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE1= ' + str(TheBet))
    if (Pole[6] == Pole[7] == Pole[8] == PolePer[0] or Pole[6] == Pole[7] == Pole[8] == PolePer[1] or Pole[6] == Pole[7] == Pole[8] == PolePer[2]):
        TheBet = 5* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE3= ' + str(TheBet))
    if (Pole[0] == Pole[4] == Pole[8] == PolePer[0] or Pole[0] == Pole[4] == Pole[8] == PolePer[1] or Pole[0] == Pole[4] == Pole[8] == PolePer[2]):
        TheBet = 5* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE4= ' + str(TheBet))
    if (Pole[6] == Pole[4] == Pole[2] == PolePer[0] or Pole[6] == Pole[4] == Pole[2] == PolePer[1] or Pole[6] == Pole[4] == Pole[2] == PolePer[2]):
        TheBet = 5* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE5= ' + str(TheBet))
    if Pole[3] == Pole[4] == Pole[5] == PolePer[3]:
        TheBet = 20* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE1= ' + str(TheBet))
    if Pole[6] == Pole[7] == Pole[8] == PolePer[3]:
        TheBet = 20* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE3= ' + str(TheBet))
    if Pole[0] == Pole[1] == Pole[2] == PolePer[3]:
        TheBet = 20* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE2= ' + str(TheBet))
    if Pole[0] == Pole[4] == Pole[8] == PolePer[3]:
        TheBet = 20* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE4= ' + str(TheBet))
    if Pole[6] == Pole[4] == Pole[2] == PolePer[3]:
        TheBet = 20* int(Bet)
        i = i + 1
        u = u + TheBet
        print('Выигрыш LINE5= ' + str(TheBet))
    if i == 0:
            print('Выигрыш равен 0!')
    return u
            

def Stavka():
    while True:
        print('Сделайте Вашу ставку(5,10,25,50,100 или 500), BET: ', end='')
        Bet = input()
        print()
        if Bet not in ['5', '10', '25', '50', '100', '500']:
            print()
        else:
            return Bet
            
            
    
#ТЕЛО ИГРЫ
Balance = 2000
PolePer = ['O', 'X', 'Z', 'Y']

while True:
    print()
    print('                 WELCOME IN CASINO "LUCKYMAN"')
    print('               (OOO,XXX,ZZZ = bet*5 YYY = bet*20)')
    print('                         win CASH>10000')
    print()
    print('YOUR CASH : ' + str(Balance) + ' рублей')
    print()

    BetR = int(Stavka())

    
    if BetR <= Balance:
        Pole = GamePole()
        
        print(Pole[0] + '|' + Pole[1] + '|' + Pole[2])
        print('-----')
        print(Pole[3] + '|' + Pole[4] + '|' + Pole[5])
        print('-----')
        print(Pole[6] + '|' + Pole[7] + '|' + Pole[8])
        print()
        
        Balance = Balance - BetR + Game(Pole, BetR, PolePer)
        print()
        time.sleep(5)
        os.system('cls')
    if Balance == 0:
        print('you are Looser!!! Se you soon again!!!!')
        time.sleep(5)
        break
    if Balance > 10000:
        print('You are LUCKEMAN!!!! Take my CONGRATULATIONS!!!')
        time.sleep(5)
        break
    if BetR > Balance:
        None
        
    
    

            
