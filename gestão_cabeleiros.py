import pickle

print('BEM VINDO, AO SISTEMA DE GESTÃO DE CABELEIREIROS !!!')

clientes = {} 
try:
    arq_clientes = open("clientes.dat","rb")
    clientes = pickle.load(arq_clientes)
    arq_clientes.close()
except:
    clientes = {'111': ['Edna Krabappel', 'krabappel@springfield.com', '(84) 99988-8777']} 
    arq_clientes = open('clientes.dat','wb')
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

servicos = {}
try:
    arq_servicos = open("servicos.dat","rb")
    servicos = pickle.load(arq_servicos)
    arq_servicos.close()
except:
    servicos = {'111': ['corte americano', '30 R$','30 minutos']}
    arq_servicos = open("servicos.dat","wb")
    pickle.dump(servicos, arq_servicos)
    arq_servicos.close()

agendamentos = {}
try:
    arq_agendamentos = open("agendamentos.dat","rb")
    agendamentos = pickle.load(arq_agendamentos)
    arq_agendamentos.close()
except:
    agendamentos = {'111': ['111','111', '12/10', '14:00']}
    arq_agendamentos = open("agendamentos.dat",'wb')
    pickle.dump(agendamentos, arq_agendamentos)
    arq_agendamentos.close()

# ADD com base no codigo de Flavius'

resposta = ''


while resposta != '0':

    print('''
[1]Gerenciar clientes
[2]Gerenciar serviços
[3]Gerenciar agendamentos
[4]Ver relatorios
[5]Sobre o sistema
[0]Sair
    ''')

    #MODULO DE CLIENTES
    resposta = input('escolha uma das opções:')
   
    if resposta == '1':
        print('''
######### MODULO DE CLIENTES ##########
                                                 
[1] Cadastrar cliente               
[2] Remover cliente
[3] Editar informações de cliente
[4] Pesquisar cliente
[5] Listar clientes
             
######################################
        ''')

        resposta = input('escolha uma das opções:')

        if resposta == '1':
            cpf_cliente = input('digite o cpf do cliente:')
            nome_cliente = input('digite o nome do cliente:')
            celular_cliente = input('digite o numero do celular do cliente:')
            email_cliente = input('digite o email do cliente:')

            clientes[cpf_cliente] = [nome_cliente, email_cliente, celular_cliente] 

            print('''
#######################################
## Cliente Cadastrado com sucesso!!! ##
#######################################
                  ''') 

            print('Clientes:',clientes)

            
        
        elif resposta == '2':
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
                    

            

        elif resposta == '3':
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
           
        
        elif resposta == '4':
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

        elif resposta == '5':
            print('''
##########################
## Lista de Clientes!!! ##
##########################
                  ''') 
            print(clientes)
        
        else:
            print('Nenhuma das opções!!!')


    #MODULO DE SERVIÇOS
    elif resposta == '2':
        print('''
####### MODULO DE SERVIÇOS #######
             
[1] Cadastrar serviço
[2] Remover serviço
[3] Editar informações de serviço
[4] Pesquisar serviço
[5] Listar serviços
             
#################################
        ''')

        resposta = input('escolha uma das opções:')

        if resposta == '1':
            codigo_servico = input('Digite o id/codigo so serviço:')
            nome_servico = input('Digite o nome do serviço (ex: corte):')
            valor_servico = input('Digite o valor do serviço(R$):')
            duracao_servico = input('Digite a duração estimada (ex: 30 min): ')
            
            servicos[codigo_servico] = [nome_servico,valor_servico,duracao_servico]
            
            print('''
#######################################
## Serviço Cadastrado com sucesso!!! ##\
#######################################
                  ''') 

            print('Serviços:',servicos)

        elif resposta == '2':
            codigo_servico = input('Digite o codigo do serviço:')

            if codigo_servico in servicos:
                print("##### Serviços encontrado:")
                print("##### Nome     :", servicos[codigo_servico][0])
                print("##### Valor    :", servicos[codigo_servico][1])
                print("##### Duração  :", servicos[codigo_servico][2])

                comfirmar_excluir = input('Digite [s] para confirmar que deseja excluir:')

                if comfirmar_excluir.lower() == 's':
                    del servicos[codigo_servico]

                    print('''
######################################
## Serviço  Removido com sucesso!!! ##
######################################
                        ''')
                    
                    print('serviços',servicos)

                else:
                    print('Remoção do serviço cancelada!!!')
            
            else:
                print('Serviço não encontrado!!!')
        elif resposta == '3':
            codigo_servico = input('Digite o codigo do serviço:')
            
            if codigo_servico in servicos:
                print("##### Serviço encontrado:")
                print("##### Nome     :", servicos[codigo_servico][0])
                print("##### Valor    :", servicos[codigo_servico][1])
                print("##### Duração  :", servicos[codigo_servico][2])

                novo_nome_servico = input('Digite o novo nome do serviço:')
                novo_valor_servico = input('Digite o novo valor do serviço (R$):')
                nova_duracao_servico = input('Digite a nova duração do serviço:')

                servicos[codigo_servico] = [novo_nome_servico, novo_valor_servico, nova_duracao_servico]

                print('''
####################################
## Serviço editado com sucesso!!! ##
####################################
                    ''')

                print('Serviços:', servicos)
            
            else:
                print('Serviço não encontrado!!!')

        elif resposta == '4':
            codigo_servico = input('Digite o codigo do serviço que deseja realizar a pesquisa:')
            
            if codigo_servico in servicos:
                print("##### Serviço encontrado:")
                print("##### Nome     :", servicos[codigo_servico][0])
                print("##### Valor    :", servicos[codigo_servico][1])
                print("##### Duração  :", servicos[codigo_servico][2])
                print('''
#######################################
## Pesquisa realizada com sucesso!!! ##
#######################################
                        ''')
                
            else:
                print('Serviço não encontrado!!!')

        elif resposta == '5':
            print('''
##########################
## Lista de Serviços!!! ##
##########################
                  ''') 
            print(servicos)
        
        else:
            print('Nenhuma das opções!!!')



#MODULO DE AGENDAMENTOS
    elif resposta == '3':
        print('''
####### MODULO DE AGENDAMENTOS #######
             
[1] Agendar horário
[2] Cancelar agendamento
[3] Reagendar horário
[4] Pesquisar agendamento
[5] Listar agendamentos
             
######################################
        ''')

        resposta = input('escolha uma das opções:')

        
        if resposta == '1':
            codigo_agendamento = input('Digite um id/codigo para o agendamento: ')
            cpf_cliente = input('Digite o CPF do cliente: ')
            codigo_servico = input('Digite o id/código do serviço: ')
            data_agendamento = input('Digite a data (ex: 12/10): ')
            horario_agendamento = input('Digite o horário (ex: 14:00): ')

            
            if cpf_cliente not in clientes:
                print('-> Aviso: Este CPF de cliente ainda não está cadastrado!')
            if codigo_servico not in servicos:
                print('-> Aviso: Este código de serviço ainda não está cadastrado!')

            
            agendamentos[codigo_agendamento] = [cpf_cliente, codigo_servico, data_agendamento, horario_agendamento]

            print('''
##########################################
## Agendamento realizado com sucesso!!! ##
##########################################
                  ''') 
            print('Agendamentos:', agendamentos)

        elif resposta == '2':
            codigo_agendamento = input('Digite o código do agendamento que deseja cancelar: ')

            if codigo_agendamento in agendamentos:
                print("##### Agendamento encontrado:")
                print("##### CPF Cliente :", agendamentos[codigo_agendamento][0])
                print("##### Cód. Serviço:", agendamentos[codigo_agendamento][1])
                print("##### Data        :", agendamentos[codigo_agendamento][2])
                print("##### Horário     :", agendamentos[codigo_agendamento][3])

                confirmar_excluir = input('Digite [s] para confirmar o cancelamento: ')

                if confirmar_excluir.lower() == 's':
                    del agendamentos[codigo_agendamento]

                    print('''
##########################################
## Agendamento cancelado com sucesso!!! ##
##########################################
                        ''')
                    print('Agendamentos:', agendamentos)
                else:
                    print('Cancelamento abortado!!!')
            else:
                print('Agendamento não encontrado!!!')

        elif resposta == '3':
            codigo_agendamento = input('Digite o código do agendamento que deseja reagendar: ')

            if codigo_agendamento in agendamentos:
                print("##### Agendamento atual:")
                print("##### CPF Cliente :", agendamentos[codigo_agendamento][0])
                print("##### Cód. Serviço:", agendamentos[codigo_agendamento][1])
                print("##### Data        :", agendamentos[codigo_agendamento][2])
                print("##### Horário     :", agendamentos[codigo_agendamento][3])

                novo_cpf = input('Digite o novo CPF do cliente (ou repita o atual): ')
                novo_servico = input('Digite o novo código do serviço (or repita o atual): ')
                nova_data = input('Digite a nova data: ')
                novo_horario = input('Digite o novo horário: ')

                agendamentos[codigo_agendamento] = [novo_cpf, novo_servico, nova_data, novo_horario]

                print('''
############################################
## Reagendamento realizado com sucesso!!! ##
############################################
                    ''')
                print('Agendamentos:', agendamentos)
            else:
                print('Agendamento não encontrado!!!')
 

        elif resposta == '4':
            codigo_agendamento = input('Digite o código do agendamento que deseja pesquisar: ')

            if codigo_agendamento in agendamentos:
                print("##### Agendamento encontrado:")
                print("##### CPF Cliente :", agendamentos[codigo_agendamento][0])
                print("##### Cód. Serviço:", agendamentos[codigo_agendamento][1])
                print("##### Data        :", agendamentos[codigo_agendamento][2])
                print("##### Horário     :", agendamentos[codigo_agendamento][3])
                print('''
#######################################
## Pesquisa realizada com sucesso!!! ##
#######################################
                        ''')
            else:
                print('Agendamento não encontrado!!!')

        elif resposta == '5':
            print('''
#############################
## Lista de Agendamentos!!! ##
#############################
                  ''') 
            print(agendamentos)
        
        else:
            print('Nenhuma das opções!!!')

    
    #MODULO DE RELATÓRIOS
    elif resposta == '4':
        print('''
             ### MODULO DE RELATÓRIOS ###
             
             [1] Lista geral de clientes
             [2] Lista geral de serviços
             [3] Lista geral de agendamentos
             
            ############################
        ''')

        resposta = input('escolha uma das opções:')

        if resposta == '1':
            print('... Ainda não temos relatorios ...')
        elif resposta == '2':
            print('... Ainda não temos relatorios ...')
        elif resposta == '3':
           print('... Ainda não temos relatorios ...')
        else:
            print('Nenhuma das opções!!!')


    
    #SOBRE O SISTEMA
    elif resposta == '5':
        print('''
             ####################### SOBRE O SISTEMA #########################
             
             Sistema de Gestão de Cabeleireiros
             Desenvolvido para controle de clientes, serviços e agendamentos.
             Desenvolvedor: Ruan Allyson de Araújo Felix
             
            ##################################################################
        ''')

    #SAIR
    elif resposta == '0':
        print('Saindo do sistema... Até logo!')
        break
    
    else:
        print('Nenhuma das opções!!!')
    
   

arq_clientes = open("clientes.dat", "wb")
pickle.dump(clientes, arq_clientes)
arq_clientes.close()

arq_servicos = open("servicos.dat", "wb")
pickle.dump(servicos, arq_servicos)
arq_servicos.close()

arq_agendamentos = open("agendamentos.dat", "wb")
pickle.dump(agendamentos, arq_agendamentos)
arq_agendamentos.close()

#sistema de gestão para cabeleireiros
#1 crud para clientes (modulos)
#2 crud para servios (modulos)
#3 crud para agendamentos (modulos)
#4 modulo relatorios 
#5 modulo sobre o sistema 
#0 sair
