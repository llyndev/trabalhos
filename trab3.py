#Função para verificar se a escolha do usúario é valida 
def escolha_servico(pergunta):
    #Lista
    opcoes = ['DIG', 'ICO','IPB','FOT']
    while True:
        #Verifica se o que o usúario digitou esta na lista
        x = input(pergunta).upper()
        if x in opcoes:
            return x
        #Caso não estiver na list executa o print
        else:
            print('Escolha inválida, entre com o tipo de serviço novamente\n')
            
#Função para verificar a quantidade de páginas que o usúario deseja sendo o máximo 20000
def num_pagina():
    while True:
        try:
            num_pag = int(input('\nDigite o número de páginas: '))
            #Verificando a quantidade de páginas e já aplicando o desconto dependendo da quantidade dela 
            if num_pag >= 20000:
                print('Não aceitamos tantas páginas de uma vez.\nPor favor, entre com o número de páginas novamente.\n')
            elif num_pag < 20:
                return num_pag
            elif num_pag >= 20 and num_pag < 200:
                return int(num_pag * 0.85)
            elif num_pag >= 200 and num_pag < 2000:
                return int(num_pag * 0.80)
            elif num_pag >= 2000 and num_pag < 20000:
                return int(num_pag * 0.75)
        #Caso o usúario digitou algum número real ou caracter inválido e executado o print
        except ValueError:
            print('Digite um número inteiro\n')
            
#Função que verifica se o usúario deseja adcionar algum tipo de serviço
def servico_extra():
    while True:
            print('\nDeseja adicionar algum serviço?')
            print('1 - Encadernação Simples - R$ 15.00')
            print('2 - Encadernação Capa Dura - R$ 40.00')
            print('0 - Não deseja mais nada')
            escolha = input('>>')
            if escolha in ['1', '2', '0']:
                if escolha == '1':
                    return 15
                elif escolha == '2':
                    return 40
                else:
                    return 0
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

#Estrutura de repetição que recebe todos os dados das funções acima e verifica qual tipo de serviço, quantidade de páginas e se o usúario deseja o serviço extra
while True:
    print('Bem-Vindo a Copiadora do Weslley Alves\n')
    op = escolha_servico('Entre com o tipo de serviço desejado\nDIG - Digitalização\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia\n>> ')
    if op == 'DIG':
        num_paginas = num_pagina()
        servico = 1.10
        extra = servico_extra()
    if op == 'ICO':
        num_paginas = num_pagina()
        servico = 1
        extra = servico_extra()
    if op == 'IPB':
        num_paginas = num_pagina()
        servico = 0.40
        extra = servico_extra()
    if op == 'FOT':
        num_paginas = num_pagina()
        servico = 0.20
        extra = servico_extra()
        
    total = (servico * num_paginas) + extra
        
    print(f'Total R${total:.2f} (serviço: R${servico:.2f} * páginas: R$ {num_paginas:.2f} + extra: R${extra:.2f})')
    break