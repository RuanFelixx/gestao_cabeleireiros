from clientes import modulo_clientes
from servicos import modulo_servicos
from agendamentos import modulo_agendamentos
from relatorios import modulo_relatorios
from sobre import modulo_sobre
import pickle


print('BEM VINDO, AO SISTEMA DE GESTÃO DE CABELEIREIROS !!!')

clientes = {} 
try:
    arq_clientes = open("clientes.dat","rb")
    clientes = pickle.load(arq_clientes)
    arq_clientes.close()
except:
    clientes = {'111.111.111-00': ['Edna Krabappel', 'krabappel@springfield.com', '(84) 99988-8777', True]} 
    arq_clientes = open('clientes.dat','wb')
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

servicos = {}
try:
    arq_servicos = open("servicos.dat","rb")
    servicos = pickle.load(arq_servicos)
    arq_servicos.close()
except:
    servicos = {'111': ['corte americano', '30 R$','30 minutos', True]}
    arq_servicos = open("servicos.dat","wb")
    pickle.dump(servicos, arq_servicos)
    arq_servicos.close()

agendamentos = {}
try:
    arq_agendamentos = open("agendamentos.dat","rb")
    agendamentos = pickle.load(arq_agendamentos)
    arq_agendamentos.close()
except:
    agendamentos = {'111': ['111-111-111.00','111', '12/10', '14:00', True]}
    arq_agendamentos = open("agendamentos.dat",'wb')
    pickle.dump(agendamentos, arq_agendamentos)
    arq_agendamentos.close()

# ADD com base no codigo de Flavius

resposta_prin = ''


while resposta_prin != '0':
    
    print('''
[1]Gerenciar clientes
[2]Gerenciar serviços
[3]Gerenciar agendamentos
[4]Ver relatorios
[5]Sobre o sistema
[0]Sair
    ''')


    resposta_prin = input('escolha uma das opções:')

    #MODULO DE CLIENTES
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
        modulo_sobre()

    #SAIR
    elif resposta_prin == '0':
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
