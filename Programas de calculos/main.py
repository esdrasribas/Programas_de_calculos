from opcao import selecao
from time import sleep
from Simulador import jogarDados
from advinhar import Advinhe_valor
while True:

    opcao = selecao()
    if opcao == '0':
        print('\n\tVolte Sempre!')
        break
    
    elif opcao == '1':
        num_opcao = int(input('\n\tDigite o número para multiplicar: '))
        for i in range(1,11):
            print(f'{num_opcao} x {i} = {num_opcao * i}')
            sleep(0.2)
            pass
    
    elif opcao == '2':
        num_opcao = int(input('\n\tDigite o número queira multiplcar por ele mesmo: '))
        sleep(0.2)
        print(f'O resultado é: {num_opcao * num_opcao}')
        sleep(1)
    
    elif opcao == '3':
        jogarDados()
        sleep(2)
        continue
    
    elif opcao == '4':
        valor_f = int(input('\n\tDigite o valor final: '))
        j = 0
        i = 1
        print(j)
        print(i)
        for p in range(0,valor_f):
            p += i + j
            sleep(0.3)
            print(p)
            t = i
            i = p
            j = t
        sleep(0.3)
    elif opcao == '5':
        Advinhe_valor()
        sleep(2)
        continue
    
    
    
        




            
    #     elif num_opcao == 's':
    #         num_opcao1 = int(input('\n\tDigite o Primeiro número: '))
    #         num_opcao2 = int(input('\n\tigite o Segundo número: '))
    #         print(f'\n\t{num_opcao1} x {num_opcao2} = {num_opcao1 * num_opcao2}')