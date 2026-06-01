print('BEM VINDO, AO SISTEMA DE GESTÃO DE CABELEIREIROS !!!')

clientes = []

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
    resposta = int(input('escolha uma das opções:'))
   
    if resposta == 1:
        print('''
             ### MODULO DE CLIENTES ###
             
             [1] Cadastrar cliente
             [2] Remover cliente
             [3] Editar informações de cliente
             [4] Pesquisar cliente
             [5] Listar clientes
             
            ############################
        ''')

        resposta = int(input('escolha uma das opções:'))

        if resposta == 1:
            nome_cliente = input('digite o nome do cliente:')
            cpf_cliente = input('didte o cpf do cliente:')
            celular_cliente = input('digite o numero do celular do cliente:')
            email_cliente = input('digite o email do cliente:')

            print('Cadastrado com sucesso!!!') #ta mentindo sim, pelo menos por enquanto
        
        elif resposta == 2:
            print('cliente removido com sucesso!!!')

        elif resposta == 3:
            print('Edição do cliente, realiazada com sucesso!!!')
        
        elif resposta == 4:
            print('Pesquisa realizada com sucesso!!!')

        elif resposta == 5:
            print('Lista dos clientes!!!')
        
        else:
            print('Nenhuma das opções!!!')

    #MODULO DE SERVIÇOS
    elif resposta == 2:
        print('''
             ### MODULO DE SERVIÇOS ###
             
             [1] Cadastrar serviço
             [2] Remover serviço
             [3] Editar informações de serviço
             [4] Pesquisar serviço
             [5] Listar serviços
             
            ############################
        ''')

        resposta = int(input('escolha uma das opções:'))

        if resposta == 1:
            print('Serviço cadastrado com sucesso!!!')
        elif resposta == 2:
            print('Serviço removido com sucesso!!!')
        elif resposta == 3:
            print('Edição do serviço realizada com sucesso!!!')
        elif resposta == 4:
            print('Pesquisa de serviço realizada com sucesso!!!')
        elif resposta == 5:
            print('Lista dos serviços!!!')
        else:
            print('Nenhuma das opções!!!')

    #MODULO DE AGENDAMENTOS
    elif resposta == 3:
        print('''
             ### MODULO DE AGENDAMENTOS ###
             
             [1] Agendar horário
             [2] Cancelar agendamento
             [3] Reagendar horário
             [4] Pesquisar agendamento
             [5] Listar agendamentos
             
            ############################
        ''')

        resposta = int(input('escolha uma das opções:'))

        if resposta == 1:
            print('Agendamento realizado com sucesso!!!')
        elif resposta == 2:
            print('Agendamento cancelado com sucesso!!!')
        elif resposta == 3:
            print('Reagendamento realizado com sucesso!!!')
        elif resposta == 4:
            print('Pesquisa de agendamento realizada com sucesso!!!')
        elif resposta == 5:
            print('Lista dos agendamentos!!!')
        else:
            print('Nenhuma das opções!!!')
    
    #MODULO DE RELATÓRIOS
    elif resposta == 4:
        print('''
             ### MODULO DE RELATÓRIOS ###
             
             [1] Relatório de faturamento
             [2] Relatório de atendimentos por cliente
             [3] Relatório de serviços mais procurados
             
            ############################
        ''')

        resposta = int(input('escolha uma das opções:'))

        if resposta == 1:
            print('Gerando relatório de faturamento!!!')
        elif resposta == 2:
            print('Gerando relatório de atendimentos por cliente!!!')
        elif resposta == 3:
            print('Gerando relatório de serviços mais procurados!!!')
        else:
            print('Nenhuma das opções!!!')
    
    #SOBRE O SISTEMA
    elif resposta == 5:
        print('''
             ### SOBRE O SISTEMA ###
             
             Sistema de Gestão de Cabeleireiros
             Desenvolvido para controle de clientes, serviços e agendamentos.
             Desenvolvedor: Ruan Allyson de Araújo Felix
             
            ############################
        ''')

    #SAIR
    elif resposta == 0:
        print('Saindo do sistema... Até logo!')
        break
    
    else:
        print('Nenhuma das opções!!!')
    
   

   
#sistema de gestão para cabeleireiros
#1 crud para clientes (modulos)
#2 crud para servios (modulos)
#3 crud para agendamentos (modulos)
#4 modulo relatorios 
#5 modulo sobre o sistema 
#0 sair