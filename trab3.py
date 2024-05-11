def escolha_servico(pergunta):
    opcoes = ['DIG', 'ICO','IPB','FOT']
    while True:
        x = input(pergunta).upper()
        if x in opcoes:
            return x
        else:
            print('Escolha inválida, entre com o tipo de serviço novamente\n')
            
def num_pagina():
    while True:
        try:
            num_pag = int(input('\nDigite o número de páginas: '))
            if num_pag >= 20000:
                print('Não aceitamos tantas páginas de ma vez.\nPor favor, entre com o número de páginas novamente.\n')
            elif num_pag < 20:
                return num_pag
            elif num_pag >= 20 and num_pag < 200:
                return int(num_pag * 0.85)
            elif num_pag >= 200 and num_pag < 2000:
                return int(num_pag * 0.80)
            elif num_pag >= 2000 and num_pag < 20000:
                return int(num_pag * 0.75)
        except ValueError:
            print('Digite um número inteiro\n')
            
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
        
    print(f'Total R${total:.2f} (serviço: R${servico} * páginas: R$ {num_paginas} + extra: R${extra})')
    break