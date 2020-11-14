from time import sleep
from random import randrange

print('-=' * 30)
print('{:^60}'.format('JOGO DE ADIVINHAÇÃO'))
print('-=' * 30)

sleep(1)

while True:
    print('\nPense em um numero!!!}')
    while True:
        r = str(input('\033[35;32mPensou? [S/N] \033[m')).upper()
        if r in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N!')
    if r == 'S':
        break

while True:
    print('\nSome ele mais ele! Ex.: 1 + 1')
    while True:
        r2 = str(input('\033[35;32mSomou? [S/N] \033[m')).upper()
        if r2 in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N!')
    if r2 == 'S':
        break

while True:
    n = randrange(2, 20, 2)
    print('\nAgora some {} ao valor da soma anterior!'.format(n))
    while True:
        r3 = str(input('\033[35;32mSomou? [S/N] \033[m')).upper()
        if r3 in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N!')
    if r3 == 'S':
        break

while True:
    print('\nAgora divida por 2! ')
    divi = n / 2
    while True:
        r4 = str(input('\033[35;32mDividiu? [S/N] \033[m')).upper()
        if r4 in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N!')
    if r4 == 'S':
        break

while True:
    print('\nMenos o primeiro numero que você pensou')
    while True:
        r5 = str(input('\033[35;32mSubtraiu? [S/N] \033[m')).upper()
        if r5 in "SN":
            break
        print('ERRO! Por favor, digite apenas S ou N!')
    if r5 == "S":
        break

print('\n\n')

print('PROCESSANDO', end='')
for c in range(15):
    print('.', end='')
    sleep(0.2)

print('\n')

print('O resultado é \033[7;32;36m{}\033[m'.format(divi))