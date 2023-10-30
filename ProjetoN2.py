import os
import re

#ARMAZENA TODAS AS INFORMAÇÔES DE CADASTRO:
cadastro=[]
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
#validar email
emails=[]


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
    
    if op==1 and cadastro == [] :
        print("MACK BANK - CADASTRO DE CONTA")
        def cadastro_cliente():
            #CADASTRO DO CLIENTE:
            num_conta= 5656
            #INPUTS PARA RECEBER INFORMAÇÕES DE CADASTRO:
            while len(cadastro) != 6:
                nome_cliente=input("NOME DO CLIENTE:")
                telefone=int(input("TELEFONE.......: "))
                def validador_email(email):
                    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                    return re.match(padrao,email)
                email=input("EMAIL..........: ")  
                if  validador_email(email):
                    emails.append(email)
                    
                else:
                    print("-----EMAIL INVALIDO-----")
                    

                saldo_inicial=float(input("SALDO INICIAL..: "))
                limite_credito=float(input("LIMITE DE CRÉDITO: "))
                senha=int(input("SENHA...............: "))
                vali_senha=int(input("REPITA A SENHA.....: "))

                # VALIDADOR DAS INFORMAÇÔES:
                if nome_cliente == str():
                    print(".......NOME INVALIDO!........")
                    print("\n Aperte <enter> para cadastrar novamente...")    

                elif telefone < 101010101:
                    print(".......TELEFONE INVALIDO!........")
                    input("\n Aperte <enter> para cadastrar novamente...")    

                elif  saldo_inicial < 1000 :
                    print(".......SALDO INVALIDO!........")
                    input("\n Aperte <enter> para cadastrar novamente...")    

                elif  limite_credito < 0 :
                    print(".......LIMITE DE CREDITO INVALIDO!........")
                    input("\n Aperte <enter> para cadastrar novamente...")    

                elif  senha < 000000 and senha > 000000:
                    print(".......SENHA INVALIDA!........")
                    input("\n Aperte <enter> para cadastrar novamente...")    

                elif  vali_senha!=senha  :
                    print(".......SENHA INVALIDA!........")
                    input("\n Aperte <enter> para cadastrar novamente...")    

                #REGISTRA AS INFORMAÇÔES E FINALIZA O CADASTRO:
                else:
                    cadastro.append(num_conta)
                    cadastro.append(nome_cliente)
                    cadastro.append(telefone)
                    cadastro.append(senha)
                    if len(emails)==1:
                        cadastro.append(email)
                    cadastro.append(vali_senha)
                    saldo.append(saldo_inicial)
                    lmt_credito.append(limite_credito)
                    if len(cadastro)==6:
                        print("CADASTRO FINALIZADO")
                     
            input("\n Aperte <enter> para continuar...")    

        cadastro_cliente()    
    
    #Verifica se ja existe uma conta :
    elif op==2 and  len(cadastro) == 6:

        print("MACK BANK - SAQUE DA CONTA")
        num_conta=int(input("INFORME O NÚMERO DA CONTA: "))
       
        if num_conta==5656:
            print(f"NOME DO CLIENTE:{cadastro[1]}")
            deposito=float(input("VALOR DO DEPOSITO: "))

            #Soma e substitui o valor do saldo inicial
            novo_saldo=deposito+saldo[0]
            saldo[0]=novo_saldo
            
            depositos.append(novo_saldo)
            print("DEPÓSITO REALIZADO COM SUCESSO!")
            
        else:
            print("NUMERO DA CONTA INVÁLIDO")
        input("\n Aperte <enter> para continuar...")

    #Caso o usuário errar a senha 3 vezes essa opção fica bloqueada 
    elif op== 3 and len(cadastro) == 6 and len(contsenha)!=1:
        print("MACK BANK - DEPÓSITO EM CONTA")

        def sacar():
            num_conta=int(input("INFORME O NÚMERO DA CONTA: "))

            if num_conta==5656:
                print(f"NOME DO CLIENTE: {cadastro[1]}")
                senha=int(input("INFORME A SENHA: "))
                cont_senha=1
            
                while cont_senha <3 and  senha != cadastro[5]:
                    cont_senha+=1
                    senha=int(input("INFORME A SENHA: "))
                    if cont_senha==3 and senha!=cadastro[5]:
                        print("BLOQUEADO")
                        contsenha.append(cont_senha)
                        input("\n Aperte <enter> para continuar...")

                if senha == cadastro[5]:
                    saque=float(input("VALOR DO SAQUE:R$ "))

                    if saque > 0 and saque <= saldo[0] :
                        novo_saldo1=  saldo[0] - saque
                        saldo[0]=novo_saldo1
                        saques.append(novo_saldo1)
                       

                        print("SAQUE REAIZADO COM SUCESSO")
                        input("\n Aperte <enter> para continuar...")
                    elif saque > saldo[0] and saque <=lmt_credito[0]:
                        novo_saldo2= lmt_credito[0]-saque 
                        novo_saldo3= saldo[0] - saque
                        lmt_credito[0]=novo_saldo2
                        saldo[0]=novo_saldo3
                        saques.append(novo_saldo2)
                        
                        

                        print("SAQUE REAIZADO COM SUCESSO")
                        print("VOCÊ ESTA USANDO SEU LIMITE DE CRÉDITO")
                        input("\n Aperte <enter> para continuar...")
                    else:
                        print("SALDO INSUFICIENTE")
                        input("\n Aperte <enter> para continuar...")
            else:
                print("NUMERO DA CONTA ERRADO")
                input("\n Aperte <enter> para continuar...")
        sacar()
        
    elif op == 4 and  len(cadastro) == 6 and len(contsenha)!=1: 
        
        def consulta_saldo():
            num_conta=int(input("INFORME O NÚMERO DA CONTA: "))

            if num_conta==5656:
                print(f"NOME DO CLIENTE: {cadastro[1]}")
                senha=int(input("INFORME A SENHA: "))
                cont_senha=1
            
                while cont_senha <3 and  senha != cadastro[5]:
                    cont_senha+=1
                    senha=int(input("INFORME A SENHA: "))
                    if cont_senha==3 and senha!=cadastro[5]:
                        print("BLOQUEADO")
                        contsenha.append(cont_senha)
                        input("\n Aperte <enter> para continuar...")
        
                if senha == cadastro[5]:
                    print(f"SALDO EM CONTA:{saldo[0]} ")
                    print(f"LIMITE DE CRÉDITO:{lmt_credito[0]} ")
                    input("\n Aperte <enter> para continuar...")
            else:
                print("NUMERO DA CONTA ERRADO")
                input("\n Aperte <enter> para continuar...")

        consulta_saldo()
    
    elif op == 5 and len(cadastro) == 6 and len(contsenha)!=1:
        def consulta_extrato():
            num_conta=int(input("INFORME O NÚMERO DA CONTA: "))

            if num_conta==5656:
                print(f"NOME DO CLIENTE: {cadastro[1]}")
                senha=int(input("INFORME A SENHA: "))
                cont_senha=1
            
                while cont_senha <3 and  senha != cadastro[5]:
                    cont_senha+=1
                    senha=int(input("INFORME A SENHA: "))
                    if cont_senha==3 and senha!=cadastro[5]:
                        print("BLOQUEADO")
                        contsenha.append(cont_senha)
                        input("\n Aperte <enter> para continuar...")
        
                if senha == cadastro[5] and saldo[0] > 0:
                    print(f"LIMITE DE CRÉDITO: {lmt_credito[0]}")
                    print("------ULTIMAS OPERAÇÔES----:")
                    if len(depositos) > 0:
                        print(f"DEPOSITOS:R$ +{depositos}")
                    print(f"SAQUE:R$ -{saques}")
                    print(f"SALDO EM CONTA:R$ {saldo[0]}")
                    input("\n Aperte <enter> para continuar...")
                elif senha == cadastro[5] and saldo[0]<0 :
                    print(f"LIMITE DE CRÉDITO: {lmt_credito[0]}")
                    print("------ULTIMAS OPERAÇÔES----:")
                    if len(depositos) > 0:
                        print(f"DEPOSITOS:R$ +{depositos}")
                    print(f"SAQUE:R$ -{saques}")
                    print(f"SAlDO EM CONTA:R$ {saldo[0]}")
                    print(f"-----ATENÇÂO AO SEU SALDO!-----")
                    input("\n Aperte <enter> para continuar...")

                    
            else:
                print("NUMERO DA CONTA ERRADO")
                input("\n Aperte <enter> para continuar...")


        consulta_extrato()

    elif op==6:
        print("MACK BANK -- SOBRE")
        print("Este programa foi desenvolvido por")
        print("MARCOS ANTONIO MINHANO DE CAMPOS ")
        print("TIA 42399165")
        break
    

                
            
