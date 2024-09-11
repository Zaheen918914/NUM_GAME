import random


com_num = random.randint(1,10)

chance=4
def clue():
    if com_num>5:
        print('The hidden num is greater than 5')
    elif com_num<5:
        print('The hidden num is less than 5')
while True:
    my_num = int(input('Enter a num: '))
    if my_num == com_num:
        print('YAYYYY!!!!! UUUU DIID ITTTT!!!!!!!!!!')
        break
    if my_num!=com_num:
        chance=chance-1
        clue2=input('Do u want any clue? Y/N: ')
        if clue2 =='Y':
            clue()
        print(f'You have {chance} chance left')
        if chance==0:
            print('game over')
            break


