# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python que permite criar clientes, abrir contas, realizar saques, depósitos e exibir extratos. O sistema possui uma interface baseada em texto para interação com o usuário.

## Funcionalidades

- Criar novos clientes
- Criar contas bancárias
- Realizar depósitos
- Realizar saques com limite de valor e quantidade
- Exibir extratos das transações
- Listar contas cadastradas

## Estrutura do Projeto

O sistema é composto por diversas classes que representam clientes, contas e transações:

- **Cliente**: Representa um cliente do banco, armazenando informações básicas e uma lista de contas associadas.
- **PessoaFisica**: Subclasse de Cliente que adiciona CPF, nome e data de nascimento.
- **Conta**: Representa uma conta bancária genérica, contendo saldo, histórico e operações de saque e depósito.
- **ContaCorrente**: Subclasse de Conta com limite de saque e um contador de saques diários.
- **Transacao**: Classe abstrata para representar operações financeiras.
  - **Saque**: Representa uma operação de saque e registra no histórico.
  - **Deposito**: Representa uma operação de depósito e registra no histórico.
- **Historico**: Registra todas as transações de uma conta.

## Como Executar

1. Certifique-se de ter o Python instalado (versão 3.13 ou superior).
2. Execute o script principal:

   ```sh
   python Main.py
   ```

3. Utilize o menu interativo para realizar as operações desejadas.

## Exemplo de Uso

1. Criar um novo usuário (cliente)
2. Criar uma conta para esse usuário
3. Realizar um depósito na conta
4. Sacar um valor da conta
5. Exibir o extrato da conta

## Melhorias Futuras

- Implementar persistência dos dados em um banco de dados.
- Criar uma interface gráfica para facilitar a interação.
- Implementar autenticação de usuários.

## Licença

Este projeto é de uso livre e pode ser modificado conforme necessário.
