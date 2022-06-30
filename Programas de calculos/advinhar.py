import random
import math

def Advinhe():
    menor = int(input('Digite o intervalo menor: '))
    maior = int(input('Digite o intervalo maior: '))

    x = random.randint(menor, maior)
    print('\n\tVocê tem apenas', round(math.log(maior - menor + 1, 2)),' chances para adivinhar!\n')

    chances = 0

    while chances < math.log(maior -menor + 1, 2):
        chances +=1

        numero = int(input('Digite um número: '))

        if x == numero:
            print(f'Parabéns, voce acertou! O número é {x}')
            break
            
        elif x > numero:
            print('Você adivinhou um número baixo!')
            
        elif x < numero:
            print('Você adivinhou um número alto!')
            
        if chances >= math.log(maior - menor + 1, 2):
            print('\n O número é %d'%x)
            print('\tMais sorte da próxima vez!')
