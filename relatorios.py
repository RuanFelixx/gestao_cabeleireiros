import os

def modulo_relatorios(clientes, servicos, agendamentos):
    resposta_relatorios = ''
    while resposta_relatorios != '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
###### MODULO DE RELATÓRIOS ######
             
[1] Lista geral de clientes
[2] Lista geral de serviços
[3] Lista geral de agendamentos
[4] Pesquisa por nome de cliente
[5] Pesquisa por serviço
[6] Pesquisa por 
[0] Voltar
             
#################################
        ''')
        resposta_relatorios = input('escolha uma das opções:')
        