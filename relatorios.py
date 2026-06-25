import os

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
[8] Relatório completo de agenda
[0] Voltar
#################################
        ''')
        resposta_relatorios = input('escolha uma das opções:')
        if resposta_relatorios == '1':
            print('##### CLIENTES #####')
            for cpf, dados in clientes.items():
                print('CPF:',cpf)
                print('Nome:',dados[0])
                print('Email:',dados[1])
                print('Celular:',dados[2])

        elif resposta_relatorios == '2':
            
            print()

        elif resposta_relatorios == '3':
            print()
        
        elif resposta_relatorios == '4':
            print()

        elif resposta_relatorios == '5':
            print()

        elif resposta_relatorios == '6':
            print()

        elif resposta_relatorios == '7':
            print()

        elif resposta_relatorios == '8':
            print()

        else:
            print('Nenhumas das opções!!! ')

        
