from datetime import datetime

print('''
      
    Seja bem vindo ao banco DIO
      
    1 - Sacar
    2 - Depositar
    3 - Extrato 
    4 - Para sair
      
''')

saldo = 1000
extrato = ('')
quantidade_de_transacoes = 0

while True:
    opcao = int(input('Digite a opção desejada:'))

    if opcao == 1:

        if quantidade_de_transacoes == 10:
            print('Limite de trasacoes diários atingido')

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
                extrato = extrato + f'Saque R$: -{saque:.2f}\n' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '\n'
                quantidade_de_transacoes += 1 
                print(f'Limite de saques diários restantes: {10 - quantidade_de_transacoes}')

    elif opcao == 2:
        if quantidade_de_transacoes == 10:
            print('Limite de trasacoes diários atingido')
        else:
            print(' \n Deposito')
            deposito = int(input('Digite o valor do deposito: '))
            saldo = saldo + deposito
            quantidade_de_transacoes += 1
            print(f'Deposito realizado com sucesso, seu saldo é de R$: {saldo:.2f} . Voce ainda tem {10 - quantidade_de_transacoes} transações disponíveis')
            extrato = extrato + f'Deposito R$: +{deposito:.2f}\n ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '\n'


    elif opcao == 3:
        print(extrato + f' \n Seu Saldo é R$: {saldo:.2f} ')

    elif opcao == 4:
        break
    else:
        print('Opção inválida')