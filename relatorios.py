def transformar_data(data):
    dia, mes = data.split('/')
    return int(mes)*30 + int(dia)


def modulo_relatorios(clientes, servicos, agendamentos):
    resposta_relatorios = ''
    while resposta_relatorios != '0':
        print('''
###### MODULO DE RELATÓRIOS ######
             
[1] Lista geral de clientes
[2] Lista geral de serviços
[3] Lista geral de agendamentos
[4] Buscar cliente por nome
[5] Buscar serviço pelo nome
[6] Agendamentos por período
[7] Faturamento do período
[8] Serviço mais procurado
[0] Voltar
#################################
        ''')
        resposta_relatorios = input('escolha uma das opções:')
        
        if resposta_relatorios == '1':
            print('\n##### CLIENTES #####')
            for cpf, dados in clientes.items():
                print('CPF do cliente:', cpf)
                print('Nome do cliente:', dados[0].title())
                print('Email do cliente:', dados[1])
                print('Celular do cliente:', dados[2])
                print('-' * 30)

        elif resposta_relatorios == '2':
            print('\n##### SERVIÇOS #####')
            for codigo, dados in servicos.items():
                print('Codigo do serviço:', codigo)
                print('Nome do serviço:', dados[0])
                print('Valor do serviço:', dados[1])
                print('Duração do serviço:', dados[2])
                print('-' * 30)

        elif resposta_relatorios == '3':
            print('\n##### AGENDAMENTOS #####')
            for codigo, dados in agendamentos.items():
                cpf = dados[0]
                cod_ser = dados[1]
                
                nome_cliente = clientes[cpf][0] if cpf in clientes else "Cliente Não Encontrado"
                nome_servico = servicos[cod_ser][0] if cod_ser in servicos else "Serviço Não Encontrado"
                
                print("Codigo do agendamento:", codigo)
                print("Cliente:", nome_cliente.title())
                print("Serviço:", nome_servico)
                print("Data do agendamento:", dados[2])
                print("Horário do agendamento:", dados[3])
                print('-' * 30)
        
        elif resposta_relatorios == '4':
            nome_busca = input('Digite o nome do cliente que deseja buscar:').lower()
            encontrou = False
            
            print('\n##### Resultado da Busca #####')
            for cpf, dados in clientes.items():
                if nome_busca in dados[0].lower():
                    print('CPF do cliente:', cpf)
                    print('Nome do cliente:', dados[0].title())
                    print('Email do cliente:', dados[1])
                    print('Celular do cliente:', dados[2])
                    print('-' * 30)
                    encontrou = True
            
            if not encontrou:
                print('Cliente não encontrado!!!')

        elif resposta_relatorios == '5':
            nome_busca = input('Digite o nome do serviço que deseja buscar:').lower()
            encontrou = False
            
            print('\n##### Resultado da Busca #####')
            for codigo, dados in servicos.items():
                if nome_busca in dados[0].lower():
                    print('Codigo do serviço:', codigo)
                    print('Nome do serviço:', dados[0])
                    print('Valor do serviço:', dados[1])
                    print('Duração do serviço:', dados[2])
                    print('-' * 30)
                    encontrou = True
            
            if not encontrou:
                print('Serviço não encontrado!!!')

        elif resposta_relatorios == '6':
            data_inicial = input('Digite a data inicial (ex: 10/12):')
            data_final = input('Digite a data final (ex: 20/12):')

            data_ini_num = transformar_data(data_inicial)
            data_fim_num = transformar_data(data_final)

            print(f'\n##### Agendamentos de {data_inicial} até {data_final} #####')
            for codigo, dados in agendamentos.items():
                data_num = transformar_data(dados[2])

                if data_ini_num <= data_num <= data_fim_num:
                    nome_cliente = clientes[dados[0]][0] if dados[0] in clientes else "Desconhecido"
                    nome_servico = servicos[dados[1]][0] if dados[1] in servicos else "Desconhecido"
                    
                    print("Nome do cliente:", nome_cliente.title())
                    print("Nome do serviço:", nome_servico)
                    print("Data:", dados[2])
                    print("Hora:", dados[3])
                    print('-' * 30)
                

        elif resposta_relatorios == '7':
            data_inicial = input('Digite a data inicial do faturamento (ex: 01/01):')
            data_final = input('Digite a data final do faturamento (ex: 31/01):')

            data_ini_num = transformar_data(data_inicial)
            data_fim_num = transformar_data(data_final)
            
            total = 0
            
            for codigo, dados_agenda in agendamentos.items():
                data_agenda_num = transformar_data(dados_agenda[2])
                
                if data_ini_num <= data_agenda_num <= data_fim_num and dados_agenda[4] == True:
                    cod_servico = dados_agenda[1]
                    
                    if cod_servico in servicos:
                        valor_txt = servicos[cod_servico][1]
                        valor_limpo = valor_txt.upper().replace('R$', '').replace(' ', '')
                        total += int(valor_limpo)

            print(f'\n##### Faturamento de {data_inicial} até {data_final} #####')
            print('Faturamento total do período:', total, 'R$')

        elif resposta_relatorios == '8':
            print('\n##### SERVIÇO MAIS PROCURADO #####')
            if not agendamentos:
                print("Nenhum agendamento registrado ainda.")
            else:
                contagem_servicos = {}
                for cod, dados in agendamentos.items():
                    if dados[4] == True: 
                        cod_servico = dados[1]
                        contagem_servicos[cod_servico] = contagem_servicos.get(cod_servico, 0) + 1
                
                if contagem_servicos:
                    cod_mais_procurado = max(contagem_servicos, key=contagem_servicos.get)
                    qtd = contagem_servicos[cod_mais_procurado]
                    
                    nome_servico = servicos[cod_mais_procurado][0] if cod_mais_procurado in servicos else "Serviço excluído"
                    print(f"O serviço mais procurado é: {nome_servico.lower()}")
                    print(f"Total de agendamentos realizados: {qtd} vez(es)")
                else:
                    print("Nenhum agendamento ativo encontrado.")

        elif resposta_relatorios == '0':
            print('Voltando ao menu principal...')
            
        else:
            print('Nenhuma das opções!!! ')