print('''
      
    Seja bem vindo ao banco DIO
      
    1 - Sacar
    2 - Depositar
    3 - Extrato 
    4 - Para sair
      
''')

saldo = 1000
extrato = ('')
quantidade_de_saques = 0

while True:
    opcao = int(input('Digite a opção desejada:'))

    if opcao == 1:
        if quantidade_de_saques >= 3:
            print('Limite de saques diários atingido')
        else:
            saque = int(input(' \n Digite o valor do saque: '))
            if saque < 0:
                print('Valor inválido')
            elif saque > 500:
                print('Limite por saque é de R$ 500,00')
            elif saque > saldo :
                print('Saldo insuficiente')
            else:
                saldo = saldo - saque
                print(f' \n Saque realizado com sucesso, seu saldo é de R$: {saldo:.2f}')
                extrato = extrato + f'Saque R$: -{saque:.2f}\n'
                quantidade_de_saques = quantidade_de_saques + 1
                print(f'Limite de saques diários restantes: {3 - quantidade_de_saques}')

    elif opcao == 2:
        print(' \n Deposito')
        deposito = int(input('Digite o valor do deposito: '))
        saldo = saldo + deposito
        print(f'Deposito realizado com sucesso, seu saldo é de R$: {saldo:.2f}')
        extrato = extrato + f'Deposito R$: +{deposito:.2f}\n'

    elif opcao == 3:
        print(extrato + f' \n Seu Saldo é R$: {saldo:.2f}')

    elif opcao == 4:
        break
    else:
        print('Opção inválida')