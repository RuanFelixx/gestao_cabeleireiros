import os


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
[0] Voltar
#################################
        ''')
        resposta_relatorios = input('escolha uma das opções:')
        if resposta_relatorios == '1':
            print('##### CLIENTES #####')
            for cpf, dados in clientes.items():
                print('CPF do cliente:',cpf)
                print('Nome do cliente:',dados[0])
                print('Email do cliente:',dados[1])
                print('Celular do cliente:',dados[2])

        elif resposta_relatorios == '2':
            for codigo, dados in servicos.items():
                print('Codigo do serviço:',codigo)
                print('Nome do serviço:',dados[0])
                print('Valor do serviço:',dados[1])
                print('Duração do serviço:',dados[2])
            

        elif resposta_relatorios == '3':
            for codigo, dados in agendamentos.items():
                cpf = dados[0]
                cod_ser = dados[1]
                print("Codigo do agendamento:", codigo)
                print("Cliente:", clientes[cpf][0])
                print("Serviço:", servicos[cod_ser][0])
                print("Data do agendamento:", dados[2])
                print("Horário do agendamento:", dados[3])

        
        elif resposta_relatorios == '4':
            nome_busca = input('Digite o nome dos clientes que deseja buscar:').lower()
            if nome_busca in clientes:
                print("Lista de clientes:")

                for cpf, dados in clientes.items():
                    print('CPF do cliente:',cpf)
                    print('Nome do cliente:',dados[0])
                    print('Email do cliente:',dados[1])
                    print('Celular do cliente:',dados[2])

            else:
                print('CLiente não encontrado!!!')

                

        elif resposta_relatorios == '5':
            nome_busca = input('Digite o nome do sericiço que deseja buscar:')
            if nome_busca in servicos:
                print('Lista de Serviços:')

                for codigo, dados in servicos.items():
                    print('Codigo do serviço:',codigo)
                    print('Nome do serviço:',dados[0])
                    print('Valor do serviço:',dados[1])
                    print('Duração do serviço:',dados[2])
            
            else:
                print('Serviços não encontrados!!!')

        elif resposta_relatorios == '6':
            data_inicial = input('Digite a data inicial:')
            data_final = input('Digite a data final:')

            data_inicial = transformar_data(data_inicial)
            data_final = transformar_data(data_final)

            for codigo, dados in agendamentos.items():

                data = transformar_data(dados[2])

                if data_inicial <= data <= data_final:
                    print("Nome do cliente:", clientes[dados[0]][0])
                    print("Nome do serviço:", servicos[dados[1]][0])
                    print("Data:", dados[2])
                    print("Hora:", dados[3])
                

        elif resposta_relatorios == '7':
            total = 0
            for codigo, dados in servicos.items():
                valor = dados[1]
                valor = valor.replace('R$','')
                valor = valor.strip() 
                valor = int(valor)
                total += valor

            print('Faturamento total:', total, 'R$')

        else:
            print('Nenhumas das opções!!! ')

        
