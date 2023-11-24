from random import choice
from time import sleep

def won(user: str, comp: str) -> str:
    if user == comp:
        return 'Empate!'
    
    elif user == 'PEDRA' and comp == 'TESOURA' or user == 'PAPEL' and comp == 'PEDRA' or user == 'TESOURA' and comp == 'PAPEL':
        return 'Jogador ganhou!'
    
    else:
        return 'Computador ganhou!'

while True:
    options: list = ['PEDRA', 'PAPEL', 'TESOURA']
    print('\n== OPÇÕES =='
        '\n[0] - SAIR'
        '\n[1] - PEDRA'
        '\n[2] - PAPEL'
        '\n[3] - TESOURA')

    res: int = int(input('Digite sua opção: '))
    if res == 0:
        break

    if [1, 2, 3].count(res) == 0:
        print('\nPrestenção mo fih!')
        continue


    user: str = options[res - 1]
    comp: str = choice(options)

    for label in ['\nJÔ', 'KEN', 'PÔ']:
        print(label)
        sleep(.5)

    print(f'\nJOGADOR: {user}')
    print(f'COMPUTADOR: {comp}')
    print('\n== ', won(user, comp), ' ==')

    