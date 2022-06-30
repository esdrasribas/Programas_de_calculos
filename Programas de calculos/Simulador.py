from random import randint
from time import sleep

def jogarDados():
    perguntar = input('\n\tVocê gostaria de jogar o dado? Digite [S]im ou [N]ão: ').upper()

    while True:
        
        if perguntar == 'S':
            sleep(0.7)

            sorteia = randint(1,6)
            print('Ok, então vamos continuar para o Jogo!')
            print()
            print(f'\n\tO dado caiu no: {sorteia}')
            sleep(1)

            novamente = input('\n\tDeseja continuar jogando? Digite [S]im ou [N]ão: ').upper()
            if novamente == 'N':
                print('\n\tObrigado por jogar. Volte sempre! ')
                break
            if novamente == 'S':
                continue

            else:
                print('\n\tDigite apenas o que foi solicitado. Recomece o programa...')
                break


        elif perguntar == 'N':
            print('\n\tQue pena... Volte sempre!')
            break

        else:
            print('\n\tDigite apenas o que foi solicitado. Recomece o programa...')
            break
            



    