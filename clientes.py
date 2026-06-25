import os 

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
[0] Voltar
             
######################################
        ''')
        resposta_cliente = input('escolha uma das opções:')

        if resposta_cliente == '1':
            cpf_cliente = input('digite o cpf do cliente:')
            if validar_cpf(cpf_cliente) == False:
                print('CPF invalido !')

            nome_cliente = input('digite o nome do cliente:')

            celular_cliente = input('digite o numero do celular do cliente:')
            if validar_celular(celular_cliente) == False:
                print('Numero de celular invalido !')

            email_cliente = input('digite o email do cliente:')
            if validar_email(email_cliente) == False:
                print('Email invalido !')

            clientes[cpf_cliente] = [nome_cliente, email_cliente, celular_cliente] 

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
                    del clientes[cpf_cliente]

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

                clientes[cpf_cliente] = [novo_nome_cliente, novo_email_cliente, novo_celular_cliente]

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
                
            else:
                print('Cliente não encontrado!!!')

        elif resposta_cliente == '5':
            print('''
##########################
## Lista de Clientes!!! ##
##########################
                  ''') 
            print(clientes)
        
        else:
            print('Nenhuma das opções!!!')
        

          
