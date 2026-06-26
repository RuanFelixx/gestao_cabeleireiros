import random

def gerar_codigo(servicos):

    while True:

        n1 = random.randint(0,9)
        n2 = random.randint(0,9)
        n3 = random.randint(0,9)

        cod = str(n1) + str(n2) + str(n3)

        if cod not in servicos:
            return cod


def modulo_agendamentos(clientes,servicos,agendamentos):
    resposta_agendamentos = ''
    while resposta_agendamentos != '0':
        print('''
####### MODULO DE AGENDAMENTOS #######
             
[1] Agendar horário
[2] Cancelar agendamento
[3] Reagendar horário
[4] Pesquisar agendamento
[5] Listar agendamentos
[6] Reabilitar agendamento 
[0] Voltar
             
######################################
        ''')

        resposta_agendamentos = input('escolha uma das opções:')

        
        if resposta_agendamentos == '1':
            codigo_agendamento = gerar_codigo(agendamentos)
            cpf_cliente = input('Digite o CPF do cliente: ')
            codigo_servico = input('Digite o código do serviço: ')
            data_agendamento = input('Digite a data (ex: 12/10): ')
            horario_agendamento = input('Digite o horário (ex: 14:00): ')

            
            if cpf_cliente not in clientes:
                print('Este CPF de cliente ainda não está cadastrado!')
            if codigo_servico not in servicos:
                print('Este código de serviço ainda não está cadastrado!')

            
            agendamentos[codigo_agendamento] = [cpf_cliente, codigo_servico, data_agendamento, horario_agendamento, True]

            print('''
##########################################
## Agendamento realizado com sucesso!!! ##
##########################################
                  ''') 
            print('Agendamentos:', agendamentos)

        elif resposta_agendamentos == '2':
            codigo_agendamento = input('Digite o código do agendamento que deseja cancelar: ')

            if codigo_agendamento in agendamentos:
                print("##### Agendamento encontrado:")
                print("##### CPF Cliente :", agendamentos[codigo_agendamento][0])
                print("##### Cód. Serviço:", agendamentos[codigo_agendamento][1])
                print("##### Data        :", agendamentos[codigo_agendamento][2])
                print("##### Horário     :", agendamentos[codigo_agendamento][3])

                confirmar_excluir = input('Digite [s] para confirmar o cancelamento: ')

                if confirmar_excluir.lower() == 's':
                    agendamentos[codigo_agendamento][3] = False

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

        elif resposta_agendamentos == '3':
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

                status_agendamento = agendamentos[codigo_agendamento][3]

                agendamentos[codigo_agendamento] = [novo_cpf, novo_servico, nova_data, novo_horario, status_agendamento]

                print('''
############################################
## Reagendamento realizado com sucesso!!! ##
############################################
                    ''')
                print('Agendamentos:', agendamentos)
            else:
                print('Agendamento não encontrado!!!')
 

        elif resposta_agendamentos == '4':
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
                
                if agendamentos[codigo_agendamento][3] == True:
                    print('#### Status: Ativo')

                else:
                    print('#### Status: Inativo')
            else:
                print('Agendamento não encontrado!!!')

        elif resposta_agendamentos == '5':
            print('''
##############################
## Lista de Agendamentos!!! ##
##############################
                  ''') 
            print(agendamentos)
        
        else:
            print('Nenhuma das opções!!!')