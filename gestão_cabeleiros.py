from clientes import modulo_clientes
from servicos import modulo_servicos
from agendamentos import modulo_agendamentos
from relatorios import modulo_relatorios
import pickle
import os

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

# ADD com base no codigo de Flavius

resposta_prin = ''


while resposta_prin != '0':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
[1]Gerenciar clientes
[2]Gerenciar serviços
[3]Gerenciar agendamentos
[4]Ver relatorios
[5]Sobre o sistema
[0]Sair
    ''')

    #MODULO DE CLIENTES
    resposta_prin = input('escolha uma das opções:')
   
    if resposta_prin == '1':
        modulo_clientes(clientes)
        


    #MODULO DE SERVIÇOS
    elif resposta_prin == '2':
        modulo_servicos(servicos)


    #MODULO DE AGENDAMENTOS
    elif resposta_prin == '3':
        modulo_agendamentos(clientes, servicos, agendamentos)

    
    #MODULO DE RELATÓRIOS
    elif resposta_prin == '4':
        modulo_relatorios(clientes, servicos, agendamentos)


    
    #SOBRE O SISTEMA
    elif resposta_prin == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
             #################################################################
             ####################### SOBRE O SISTEMA #########################
             #################################################################
             ###                                                           ###
             ### Sistema de Gestão de Cabeleireiros                        ###
             ###                                                           ###
             ### para controle de clientes, serviços e agendamentos.       ###
             ###                                                           ###
             ### Desenvolvedor:                                            ###
             ### Ruan Allyson de Araújo Felix                              ###
             ###                                                           ###
             ### Professor:                                                ###
             ### Flavius                                                   ###
             #################################################################                                                           
             
        ''') 

    #SAIR
    elif resposta_prin == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Saindo do sistema... Até logo!')
        break
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
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
