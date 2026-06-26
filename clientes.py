def validar_cpf(cpf):

    cpf = cpf.replace('-','')
    cpf = cpf.replace('.','')
    
    
    if len(cpf) != 11:
        return False
    
    elif not cpf.isdigit():
        return False
    
    else:
        return True
    
def validar_email(email):

    if '@' not in email:
        return False
    
    elif '.com' not in email:
        return False
    
    else:
        return True
    
def validar_celular(celular):
    
    celular = celular.replace('(','')
    celular = celular.replace(')','')
    celular = celular.replace('-','')
    celular = celular.replace(' ','')

    if len(celular) != 11:
        return False
    
    elif not celular.isdigit():
        return False
    
    else:
        return True



def modulo_clientes(clientes):
     
    resposta_cliente = ''
    while resposta_cliente != '0':
        print('''
######### MODULO DE CLIENTES ##########
                                                 
[1] Cadastrar cliente               
[2] Remover cliente
[3] Editar informações de cliente
[4] Pesquisar cliente
[5] Listar clientes
[6] Reabilitar cliente
[0] Voltar
             
######################################
        ''')
        resposta_cliente = input('escolha uma das opções:')

        if resposta_cliente == '1':
            cpf_cliente = input('digite o cpf do cliente:')
            while True:
                if validar_cpf(cpf_cliente) == False:
                    print('CPF invalido !')
                    cpf_cliente = input('digite o cpf do cliente novamente:')
                else:
                    print('CPF valido')
                    break

            nome_cliente = input('digite o nome do cliente:').lower()

            celular_cliente = input('digite o numero do celular do cliente:')
            while True:
                if validar_celular(celular_cliente) == False:
                    print('Numero de celular invalido !')
                    celular_cliente = input('digite o numero do celular do cliente novamente:')
                else:
                    print('Numeto de celular valido!')
                    break

            email_cliente = input('digite o email do cliente:')
            while True:
                if validar_email(email_cliente) == False:
                    print('Email invalido !')
                    email_cliente = input('digite o email do cliente novamente:')
                else:
                    print('Email valido!')
                    break

            clientes[cpf_cliente] = [nome_cliente, email_cliente, celular_cliente, True] 

            print('''
#######################################
## Cliente Cadastrado com sucesso!!! ##
#######################################
                  ''') 

            print('Clientes:',clientes)

            
        
        elif resposta_cliente == '2':
            cpf_cliente = input('Digite o cpf do cliente:')

            if cpf_cliente in clientes:
                print("##### Cliente encontrado:")
                print("##### Nome     :", clientes[cpf_cliente][0])
                print("##### Email    :", clientes[cpf_cliente][1])
                print("##### Celular  :", clientes[cpf_cliente][2])

                comfirmar_excluir = input('Digite [s] para confirmar que deseja excluir:')

                if comfirmar_excluir.lower() == 's':
                    clientes[cpf_cliente][3] = False

                    print('''
######################################
## Cliente  Removido com sucesso!!! ##
######################################
                        ''')
                    
                    print('clientes',clientes)

                else:
                    print('Remoção do cliente cancelada!!!')
            
            else:
                print('Cliente não encontrado!!!')
                    

            

        elif resposta_cliente == '3':
            cpf_cliente = input('Digite o cpf do cliente:')
            if cpf_cliente in clientes:
                print("##### Cliente encontrado:")
                print("##### Nome     :", clientes[cpf_cliente][0])
                print("##### Email    :", clientes[cpf_cliente][1])
                print("##### Celular  :", clientes[cpf_cliente][2])

                novo_nome_cliente = input('Digite o novo nome do cliente:')
                novo_email_cliente = input('Digite o novo email do cliente:')
                novo_celular_cliente = input('Digite o novo celular do cliente:')

                status_clientes = clientes[cpf_cliente][3]

                clientes[cpf_cliente] = [novo_nome_cliente, novo_email_cliente, novo_celular_cliente, status_clientes]

                print('''
####################################
## Cliente editado com sucesso!!! ##
####################################
                    ''')

                print('Clientes',clientes)
            
            else:
                print('Cliente não encontrado!!!')
           
        
        elif resposta_cliente == '4':
            cpf_cliente = input('Digite o cpf do cliente que deseja realizar a pesquisa:')
            if cpf_cliente in clientes:
                print("##### Cliente encontrado:")
                print("##### Nome     :", clientes[cpf_cliente][0])
                print("##### Email    :", clientes[cpf_cliente][1])
                print("##### Celular  :", clientes[cpf_cliente][2])
                print('''
#######################################
## Pesquisa realizada com sucesso!!! ##
#######################################
                        ''')
                if clientes[cpf_cliente][3] == True:
                    print('##### Status: Ativo')
                else:
                    print('#### Status: Inativo')
                
            else:
                print('Cliente não encontrado!!!')

        elif resposta_cliente == '5':
            print('''
##########################
## Lista de Clientes!!! ##
##########################
                  ''') 
            for cpf, dados in clientes.items():
                if dados[3] == True:
                    print('#### CPF:', cpf)
                    print('#### Nome:', dados[0])
                    print('#### Email:', dados[1])
                    print('#### Celular:',dados[2])

        elif resposta_cliente == '6':
            cpf_cliente = input('Digite o CPF do cliente que você deseja reativar:')

            if cpf_cliente in clientes:

                if clientes[cpf_cliente][3] == False:

                    clientes[cpf_cliente][3] = True

                    print('''
########################################
### Cliente reativado com sucesso!!!  ##
########################################
                    ''')

                else:
                    print('Este CPF já estava ativo!')
            else:
                print('Este CPF não foi cadastrado anteriormente!')
        else:
            print('Nenhuma das opções!!!')
        

          
