# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python, que permite a criação de clientes, contas correntes, depósitos, saques e a exibição de extratos. O sistema também inclui funcionalidades como limite de saques, registro de transações e um sistema de log para acompanhar as operações realizadas.

## Funcionalidades

- **Criação de Clientes**: Cadastro de clientes com nome, CPF, data de nascimento, endereço e senha.
- **Criação de Contas**: Abertura de contas correntes com limite de saque e número máximo de saques configuráveis.
- **Depósitos**: Realização de depósitos em contas.
- **Saques**: Realização de saques com validação de saldo e limite diário.
- **Extrato**: Exibição de extrato com todas as transações realizadas, saldo inicial e saldo atual.
- **Persistência de Dados**: Os dados dos clientes e contas são salvos em arquivos para persistência.
- **Autenticação**: Acesso às contas protegido por senha.
- **Log de Transações**: Todas as operações são registradas em um arquivo de log.

## Pré-requisitos

- Python 3.x
- Biblioteca `pickle` (já incluída na biblioteca padrão do Python)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Mauricioosu/sistema_bancario
   ```

2. Execute o programa:

   ```bash
   python main.py
   ```

## Uso

Ao executar o programa, você verá um menu com as seguintes opções:

- **[d] Depositar**: Realiza um depósito em uma conta.
- **[s] Sacar**: Realiza um saque de uma conta.
- **[e] Extrato**: Exibe o extrato de uma conta.
- **[nc] Nova conta**: Cria uma nova conta corrente.
- **[lc] Listar contas**: Lista todas as contas existentes.
- **[nu] Novo usuário**: Cadastra um novo cliente.
- **[sair] Sair**: Encerra o programa e salva os dados.

### Exemplo de Uso

1. **Criar um novo cliente**:
   - Selecione a opção `[nu] Novo usuário`.
   - Insira os dados solicitados (nome, CPF, data de nascimento, endereço e senha).

2. **Criar uma nova conta**:
   - Selecione a opção `[nc] Nova conta`.
   - Insira o CPF do cliente e defina o limite de saque e o número máximo de saques.

3. **Realizar um depósito**:
   - Selecione a opção `[d] Depositar`.
   - Insira o CPF do cliente e o valor do depósito.

4. **Realizar um saque**:
   - Selecione a opção `[s] Sacar`.
   - Insira o CPF do cliente e o valor do saque.

5. **Exibir extrato**:
   - Selecione a opção `[e] Extrato`.
   - Insira o CPF do cliente para visualizar o extrato.

6. **Listar contas**:
   - Selecione a opção `[lc] Listar contas` para ver todas as contas cadastradas.

7. **Sair**:
   - Selecione a opção `[sair] Sair` para encerrar o programa e salvar os dados.

## Estrutura do Projeto

- **main.py**: Arquivo principal que inicia o sistema.
- **clientes.pkl**: Arquivo que armazena os dados dos clientes.
- **contas.pkl**: Arquivo que armazena os dados das contas.
- **log.txt**: Arquivo de log que registra todas as operações realizadas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.