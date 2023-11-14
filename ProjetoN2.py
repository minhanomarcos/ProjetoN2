import os
import re
import random
import getpass

#ARMAZENA DADOS BANCÁRIOS
dados_bancarios=[]

#ARMAZENA NUMERO DA CONTA
guarda_num = 0

#Armazena o saldo:
saldo=[]

#limite de credito:
lmt_credito=[]

#deposito
depositos=[]

#controla os saques:
saques=[]

#bloqueio das funções 3,4,5:
contsenha=[]


#função de validação de email
def validador_email(email):
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(padrao,email)

#função cadastro de cliente
def cadastro_cliente():
    #CADASTRO DO CLIENTE:
    num_conta = random.randint(1000, 9999)
    print(f"NUMERO DA CONTA: {num_conta}")
    #INPUTS PARA RECEBER INFORMAÇÕES DE CADASTRO:
    while len(dados_bancarios) != 6:
        nome_cliente=input("NOME DO CLIENTE: ")
        telefone=int(input("TELEFONE.......: "))
        #validacao de email
        email = 0
        while email == 0:
            email=input("EMAIL..........: ") 
            if  validador_email(email):
                print("\n ----- EMAIL VALIDO -----")
            else:
                email = 0
                print("\n----- EMAIL INVALIDO -----")
                print("----- DIGITE NOVAMENTE -----")  
        saldo_inicial=float(input("\nSALDO INICIAL..: "))
        limite_credito=float(input("LIMITE DE CRÉDITO: "))
        senha= int(input("Cadastre uma senha de 6 caracteres: "))
        vali_senha= int(input("Confirme a senha: "))

        # VALIDADOR DAS INFORMAÇÔES:
        if nome_cliente == '' or len(nome_cliente) < 3:
            print(".......NOME INVALIDO!........")
            print("\n Aperte <enter> para cadastrar novamente...")    

        elif len(str(telefone)) < 9:
            print(".......TELEFONE INVALIDO!........")
            input("\n Aperte <enter> para cadastrar novamente...")    

        elif  saldo_inicial < 1000 :
            print(".......SALDO INVALIDO!........")
            input("\n Aperte <enter> para cadastrar novamente...")    

        elif  limite_credito < 0 :
            print(".......LIMITE DE CREDITO INVALIDO!........")
            input("\n Aperte <enter> para cadastrar novamente...")    

        elif  len(str(senha)) != 6:
            print(".......SENHA INVALIDA!........")
            input("\n Aperte <enter> para cadastrar novamente...")    

        elif  vali_senha!=senha  :
            print(".......SENHA INVALIDA!........")
            input("\n Aperte <enter> para cadastrar novamente...")    

        #REGISTRA AS INFORMAÇÔES E FINALIZA O CADASTRO:
        else:
            dados_bancarios.append(num_conta)
            dados_bancarios.append(nome_cliente)
            dados_bancarios.append(telefone)
            dados_bancarios.append(senha)
            dados_bancarios.append(email)
            dados_bancarios.append(vali_senha)
            saldo.append(saldo_inicial)
            lmt_credito.append(limite_credito)
            if len(dados_bancarios)==6:
                print("CADASTRO FINALIZADO")
                break
    input("\n Aperte <enter> para continuar...")    

#função para sacar
def sacar():
    num_conta=int(input("INFORME O NÚMERO DA CONTA: "))

    if num_conta==dados_bancarios[0]:
        print(f"NOME DO CLIENTE: {dados_bancarios[1]}")
        senha=int(input("INFORME A SENHA: "))
        cont_senha=1
    
        while cont_senha <3 and  senha != dados_bancarios[3]:
            cont_senha+=1
            senha=int(input("INFORME A SENHA: "))
            if cont_senha==3 and senha != dados_bancarios[3]:
                print("BLOQUEADO")
                contsenha.append(cont_senha)
                input("\n Aperte <enter> para continuar...")

        if senha == dados_bancarios[3]:
            saque=float(input("VALOR DO SAQUE:R$ "))

            if saque > 0 and saque <= saldo[0] :
                novo_saldo1=  saldo[0] - saque
                saldo[0]=novo_saldo1
                saques.append(-saque)      

                print("SAQUE REAIZADO COM SUCESSO")
                input("\n Aperte <enter> para continuar...")
            elif saque > saldo[0] and saque <=lmt_credito[0]:
                novo_saldo2= lmt_credito[0]-saque 
                novo_saldo3= saldo[0] - saque
                lmt_credito[0]=novo_saldo2
                saldo[0]=novo_saldo3
                saques.append(novo_saldo2)
                saques.append(-saque)
                

                print("SAQUE REAIZADO COM SUCESSO")
                print("VOCÊ ESTA USANDO SEU LIMITE DE CRÉDITO")
                input("\n Aperte <enter> para continuar...")
            else:
                print("SALDO INSUFICIENTE")
                input("\n Aperte <enter> para continuar...")
    else:
        print("NUMERO DA CONTA ERRADO")
        input("\n Aperte <enter> para continuar...")

#função consulta saldo
def consulta_saldo():
    num_conta=int(input("INFORME O NÚMERO DA CONTA: "))

    if num_conta==dados_bancarios[0]:
        print(f"NOME DO CLIENTE: {dados_bancarios[1]}")
        senha=int(input("INFORME A SENHA: "))
        cont_senha=1
    
        while cont_senha <3 and  senha != dados_bancarios[3]:
            cont_senha+=1
            senha=int(input("INFORME A SENHA: "))
            if cont_senha==3 and senha!=dados_bancarios[3]:
                print("BLOQUEADO")
                contsenha.append(cont_senha)
                input("\n Aperte <enter> para continuar...")

        if senha == dados_bancarios[3]:
            print(f"SALDO EM CONTA:{saldo[0]} ")
            print(f"LIMITE DE CRÉDITO:{lmt_credito[0]} ")
            input("\n Aperte <enter> para continuar...")
    else:
        print("NUMERO DA CONTA ERRADO")
        input("\n Aperte <enter> para continuar...")

#consulta extrato
def consulta_extrato():
    num_conta=int(input("INFORME O NÚMERO DA CONTA: "))

    if num_conta==dados_bancarios[0]:
        print(f"NOME DO CLIENTE: {dados_bancarios[1]}")
        senha=int(input("INFORME A SENHA: "))
        cont_senha=1
    
        while cont_senha <3 and  senha != dados_bancarios[3]:
            cont_senha+=1
            senha=int(input("INFORME A SENHA: "))
            if cont_senha==3 and senha!=dados_bancarios[3]:
                print("BLOQUEADO")
                contsenha.append(cont_senha)
                input("\n Aperte <enter> para continuar...")

        if senha == dados_bancarios[3] and saldo[0] > 0:
            print(f"LIMITE DE CRÉDITO: {lmt_credito[0]}")
            print("------ULTIMAS OPERAÇÔES----:")
            for i in depositos:
                if len(depositos) > 0:
                    print(f"DEPOSITOS:R$ {i}")              
                for i in saques:
                    if len(saques) > 0:
                        print(f"SAQUE:R${i}")

            print(f"SALDO EM CONTA:R$ {saldo[0]}")

            input("\n Aperte <enter> para continuar...")
        elif senha == dados_bancarios[3] and saldo[0]<0 :
            print(f"LIMITE DE CRÉDITO: {lmt_credito[0]}")
            print("------ULTIMAS OPERAÇÔES----:")
            for i in depositos:
                if len(depositos) > 0:
                    print(f"DEPOSITOS:R$ {i}")
            for i in saques:
                if len(saques) > 0:
                    print(f"SAQUE:R$ {i}")

            print(f"SAlDO EM CONTA:R$ {saldo[0]}")
            print(f"-----ATENÇÂO AO SEU SALDO!-----")
            input("\n Aperte <enter> para continuar...")

            
    else:
        print("NUMERO DA CONTA ERRADO")
        input("\n Aperte <enter> para continuar...")

fim = False
while not fim:
    os.system("Cls")
    print("----------:: MACK BANK - ESCOLHA UMA OPÇÃO::----------")
    print("(1)  CADASTRAR CONTA CORRENTE")
    print("(2)  DEPOSITAR")
    print("(3)  SACAR")
    print("(4)  CONSULTAR SALDO")
    print("(5)  CONSULTAR EXTRATO")
    print("(6)  FINALIZAR")
    op = int(input("SUA OPÇÃO: "))
    
    if op==1 and dados_bancarios == [] :
        print("MACK BANK - CADASTRO DE CONTA")
        cadastro_cliente()    
    
    #Verifica se ja existe uma conta :
    elif op==2 and  len(dados_bancarios) == 6:

        print("MACK BANK - SAQUE DA CONTA")
        num_conta = int(input("INFORME O NÚMERO DA CONTA: "))

        #válida numero da conta
        if num_conta == dados_bancarios[0]:
            print(f"NOME DO CLIENTE: {dados_bancarios[1]}")
            deposito=float(input("VALOR DO DEPOSITO: "))

            #Soma e substitui o valor do saldo inicial
            novo_saldo=deposito+saldo[0]
            saldo[0]=novo_saldo
            
            depositos.append(deposito)
            print("DEPÓSITO REALIZADO COM SUCESSO!")
            
        else:
            print("NUMERO DA CONTA INVÁLIDO")
        input("\n Aperte <enter> para continuar...")

    #Caso o usuário errar a senha 3 vezes essa opção fica bloqueada 
    elif op== 3 and len(dados_bancarios) == 6 and len(contsenha)!=1:
        print("MACK BANK - DEPÓSITO EM CONTA")
        sacar()
        
    elif op == 4 and  len(dados_bancarios) == 6 and len(contsenha)!=1: 
        consulta_saldo()
    
    elif op == 5 and len(dados_bancarios) == 6 and len(contsenha)!=1:
        consulta_extrato()

    elif op==6:
        print("MACK BANK -- SOBRE")
        print("Este programa foi desenvolvido por")
        print("MARCOS ANTONIO MINHANO DE CAMPOS | TIA: 42399165")
        print("MATHEUS FERNANDES DOS SANTOS | TIA: 32389371")
        print("LUIS FELIPE SANTOS DO NASCIMENTO | TIA: 32393059")
        break
    
    else:
        input("Opção inválida, pressione <enter> para continuar...")
    

                
            
