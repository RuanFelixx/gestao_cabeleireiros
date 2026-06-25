import os 

def modulo_servicos(servicos):
    resposta_servico = ''
    while resposta_servico != '0':
        print('''
####### MODULO DE SERVIÇOS #######
             
[1] Cadastrar serviço
[2] Remover serviço
[3] Editar informações de serviço
[4] Pesquisar serviço
[5] Listar serviços
[0] Voltar             
#################################
        ''')
        resposta_servico = input('escolha uma das opções:')

        if resposta_servico == '1':
            codigo_servico = input('Digite o id/codigo so serviço:')
            nome_servico = input('Digite o nome do serviço (ex: corte):').lower
            valor_servico = input('Digite o valor do serviço(R$):')
            duracao_servico = input('Digite a duração estimada (ex: 30 min): ')
            
            servicos[codigo_servico] = [nome_servico,valor_servico,duracao_servico]
            
            print('''
#######################################
## Serviço Cadastrado com sucesso!!! ##\
#######################################
                  ''') 

            print('Serviços:',servicos)

        elif resposta_servico == '2':
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
        elif resposta_servico == '3':
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

        elif resposta_servico == '4':
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

        elif resposta_servico == '5':
            print('''
##########################
## Lista de Serviços!!! ##
##########################
                  ''') 
            print(servicos)
        
        else:
            print('Nenhuma das opções!!!')

