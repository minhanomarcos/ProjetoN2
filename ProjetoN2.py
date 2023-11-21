#Projeto realizado pelos alunos: LUIS FELIPE SANTOS DO NASCIMENTO, MARCOS ANTONIO MINHANO DE CAMPOS e MATHEUS FERNANDES DOS SANTOS
import os
import re
import random
from getpass import getpass

# ARMAZENA DADOS BANCÁRIOS
dados_bancarios = []

# ARMAZENA NUMERO DA CONTA
guarda_num = 0

# Armazena o saldo:
saldo = []

# limite de credito:
lmt_credito = []

# deposito
depositos = []

# controla os saques:
saques = []

# controla o extrato
extrato = []

# bloqueio das funções 3,4,5:
bloqueado = False

# define our clear function
def clear():

    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

# função de validação de email
def validador_email(email):
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(padrao, str(email))


def validador_telefone(telefone):
    padrao = r"^\d{8,17}$"
    return re.match(padrao, str(telefone))


def validador_saldo(saldo):
    try:
        return float(saldo) >= 1000
    except:
        return False


def validador_credito(credito):
    try:
        return float(credito) >= 0
    except:
        return False


def valida_input(mensagem, password=False):
    valor = ""

    if password:
        valor = getpass(mensagem)
    else:
        valor = input(mensagem)

    while valor == "":
        print("=== Inválido ===")
        if password:
            valor = getpass(mensagem)
        else:
            valor = input(mensagem)

    return valor


def input_com_validacao_customizada(mensagem, func_validacao, password=False):
    valor = valida_input(mensagem, password)

    while not func_validacao(valor):
        print("=== Inválido ===")
        valor = valida_input(mensagem, password)

    return valor

def valida_senha(senha_correta):
    cont_senha = 1
    senha = input_com_validacao_customizada("INFORME A SENHA: ", lambda v: len(str(v)) == 6, password=True)

    while cont_senha < 3 and senha != senha_correta:
        cont_senha += 1
        senha = input_com_validacao_customizada("INFORME A SENHA: ", lambda v: len(str(v)) == 6, password=True)
        if cont_senha == 3 and senha != senha_correta:
            print("BLOQUEADO")
            global bloqueado
            bloqueado = True
            input("\n Aperte <enter> para continuar...")
            return False

    return True

# função cadastro de cliente
def cadastro_cliente():
    # CADASTRO DO CLIENTE:
    num_conta = random.randint(1000, 9999)
    print(f"NUMERO DA CONTA: {num_conta}")
    # INPUTS PARA RECEBER INFORMAÇÕES DE CADASTRO:
    while len(dados_bancarios) != 6:
        nome_cliente = input_com_validacao_customizada(
            "NOME DO CLIENTE: ", lambda nome: not (nome == '' or len(nome) < 3))
        telefone = int(input_com_validacao_customizada(
            "TELEFONE.......: ", validador_telefone))
        # validacao de email
        email = input_com_validacao_customizada(
            "EMAIL..........: ", validador_email)
        saldo_inicial = float(input_com_validacao_customizada(
            "SALDO INICIAL..: ", validador_saldo))
        limite_credito = float(input_com_validacao_customizada(
            "LIMITE DE CRÉDITO: ", validador_credito))
        senha = input_com_validacao_customizada(
            "Cadastre uma senha de 6 caracteres: ", lambda v: len(str(v)) == 6, password=True)
        vali_senha = input_com_validacao_customizada("Confirme a senha: ", lambda v: v == senha,  password=True)

        dados_bancarios.append(num_conta)
        dados_bancarios.append(nome_cliente)
        dados_bancarios.append(telefone)
        dados_bancarios.append(senha)
        dados_bancarios.append(email)
        dados_bancarios.append(vali_senha)
        saldo.append(saldo_inicial)
        lmt_credito.append(limite_credito)
        if len(dados_bancarios) == 6:
            print("CADASTRO FINALIZADO")
            break

    input("\n Aperte <enter> para continuar...")

# função para sacar
def sacar():
    num_conta = int(input("INFORME O NÚMERO DA CONTA: "))

    if num_conta == dados_bancarios[0]:
        print(f"NOME DO CLIENTE: {dados_bancarios[1]}")
        senha_valida = valida_senha(dados_bancarios[3])

        if senha_valida:
            saque = float(input("VALOR DO SAQUE:R$ "))

            if saque > 0 and saque <= saldo[0]:
                novo_saldo1 = saldo[0] - saque
                saldo[0] = novo_saldo1
                saques.append(-saque)
                extrato.append(-saque)

                print("SAQUE REAIZADO COM SUCESSO")
                input("\n Aperte <enter> para continuar...")
            elif saque > saldo[0] and saque <= lmt_credito[0]:
                novo_saldo2 = lmt_credito[0]-saque
                novo_saldo3 = saldo[0] - saque
                lmt_credito[0] = novo_saldo2
                saldo[0] = novo_saldo3
                saques.append(novo_saldo2)
                saques.append(-saque)
                extrato.append(-saque)

                print("SAQUE REAIZADO COM SUCESSO")
                print("VOCÊ ESTA USANDO SEU LIMITE DE CRÉDITO")
                input("\n Aperte <enter> para continuar...")
            else:
                print("SALDO INSUFICIENTE")
                input("\n Aperte <enter> para continuar...")
    else:
        print("NUMERO DA CONTA ERRADO")
        input("\n Aperte <enter> para continuar...")

#função de depósito
def deposito():
    print(f"NOME DO CLIENTE: {dados_bancarios[1]}")
    deposito = float(input("VALOR DO DEPOSITO: "))

    # Soma e substitui o valor do saldo inicial
    novo_saldo = deposito+saldo[0]
    saldo[0] = novo_saldo

    depositos.append(deposito)
    extrato.append(deposito)
    print("DEPÓSITO REALIZADO COM SUCESSO!")

# função consulta saldo


def consulta_saldo():
    num_conta = int(input("INFORME O NÚMERO DA CONTA: "))

    if num_conta == dados_bancarios[0]:
        print(f"NOME DO CLIENTE: {dados_bancarios[1]}")
        senha_valida = valida_senha(dados_bancarios[3])

        if senha_valida:
            print(f"SALDO EM CONTA:{saldo[0]:.2f} ")
            print(f"LIMITE DE CRÉDITO:{lmt_credito[0]:.2f} ")
            input("\n Aperte <enter> para continuar...")
    else:
        print("NUMERO DA CONTA ERRADO")
        input("\n Aperte <enter> para continuar...")

# consulta extrato


def consulta_extrato():
    num_conta = int(input("INFORME O NÚMERO DA CONTA: "))

    if num_conta == dados_bancarios[0]:
        print(f"NOME DO CLIENTE: {dados_bancarios[1]}")
        senha_valida = valida_senha(dados_bancarios[3])

        if senha_valida and saldo[0] > 0:
            print(f"LIMITE DE CRÉDITO: {lmt_credito[0]:.2f}")
            print("------ULTIMAS OPERAÇÔES----:")
            if len(extrato) > 0:
                for i in extrato:
                    if i > 0:
                        print(f"DEPOSITO: R$ {i:.2f}")
                    else:
                        print(f"SAQUE: R$ {i:.2f}")
            else: 
                print("Não há operações de depósitos ou saques!")
            print(f"SALDO EM CONTA:R$ {saldo[0]:.2f}")
            input("\n Aperte <enter> para continuar...")
        elif senha_valida and saldo[0] < 0:
            print(f"LIMITE DE CRÉDITO: {lmt_credito[0]:.2f}")
            print("------ULTIMAS OPERAÇÔES----:")
            if len(extrato) > 0:
                for i in extrato:
                    if i > 0:
                        print(f"DEPOSITO: R$ {i:.2f}")
                    else:
                        print(f"SAQUE: R$ {i:.2f}")
            else: 
                print("Não há operações de depósitos ou saques!")

            print(f"SAlDO EM CONTA:R$ {saldo[0]:.2f}")
            print(f"-----ATENÇÂO AO SEU SALDO!-----")
            input("\n Aperte <enter> para continuar...")

    else:
        print("NUMERO DA CONTA ERRADO")
        input("\n Aperte <enter> para continuar...")


fim = False
while not fim:
    clear()
    print(f"""
                           
                                *@@@@@@@@@@@#             
                            @@@@@@@@@@@@@@@@@@@@@,        
                        @@@@@@               @@@@@@      
                        @@@@@                     @@@@@    
                        @@@@    @@@@@       @@@@@%   @@@@%  
                    @@@@     @@@@@@     @@@@@@.    @@@@* 
                    @@@@       @@@@@@   @@@@@@       @@@@ 
                    @@@@       @@@ @@@ @@@ @@@       @@@@ 
                    @@@@       @@@  @@@@@, @@@       @@@@ 
                    @@@@     ,@@@,  @@@(  @@@@     @@@@* 
                        @@@@    @@@@@   @%  @@@@@%   @@@@%  
                        @@@@@                     @@@@@    
                        @@@@@@               @@@@@@      
                            @@@@@@@@@@@@@@@@@@@@@/        
                                *@@@@@@@@@@@#             

                                 {f"Conta: {dados_bancarios[0]}" if dados_bancarios != [] else ""}

                ================= MACK BANK =================
                ||                                         ||
                ||  1. CADASTRAR CONTA CORRENTE            ||
                ||  2. DEPOSITAR                           ||
                ||  3. SACAR                               ||
                ||  4. CONSULTAR SALDO                     ||
                ||  5. CONSULTAR EXTRATO                   ||
                ||  6. FINALIZAR                           ||
                ||                                         ||
                =============================================
""")
    op = int(input("SUA OPÇÃO: "))

    if op == 1 and dados_bancarios == []:
        print("MACK BANK - CADASTRO DE CONTA")
        cadastro_cliente()

    # Verifica se ja existe uma conta :
    elif op == 2 and len(dados_bancarios) == 6:

        print("MACK BANK - DEPÓSITO NA CONTA")
        num_conta = int(input("INFORME O NÚMERO DA CONTA: "))

        # válida numero da conta
        if num_conta == dados_bancarios[0]:
            deposito()
        else:
            print("NUMERO DA CONTA INVÁLIDO")
        input("\n Aperte <enter> para continuar...")

    # Caso o usuário errar a senha 3 vezes essa opção fica bloqueada
    elif op == 3 and len(dados_bancarios) == 6 and not bloqueado:
        print("MACK BANK - SAQUE DA CONTA")
        sacar()

    elif op == 4 and len(dados_bancarios) == 6 and not bloqueado:
        consulta_saldo()

    elif op == 5 and len(dados_bancarios) == 6 and not bloqueado:
        consulta_extrato()

    elif op == 6:
        print("MACK BANK -- SOBRE")
        print("Este programa foi desenvolvido por")
        print("MARCOS ANTONIO MINHANO DE CAMPOS | TIA: 42399165")
        print("MATHEUS FERNANDES DOS SANTOS | TIA: 32389371")
        print("LUIS FELIPE SANTOS DO NASCIMENTO | TIA: 32393059")
        break

    else:
        input("Opção inválida, pressione <enter> para continuar...")
