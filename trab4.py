#Print de Bem vindo
print('Bem vindo a Livraria do Weslley Alves')

#Lista vazia que recebe os livros
lista_livro = []
#Id recebe o ID de cada livro
id_global = 0

#Função para cadastro  do livro
def cadastrar_livro():
    #Declarando variável global
    global id_global
    #Menu cadastra livro
    print('-' * 51)
    print('-' * 15,'MENU CADASTRA LIVRO', '-' * 15)
    #A cada livro novo sendo cadastrado a variável id_global recebe um valor
    id_global += 1
    print(f'ID do Livro: {id_global}')
    nome = input('Nome do Livro: ')
    autor = input('Autor do Livro: ')
    editora = input('Editora do Livro: ')
    livro = {'id': id_global, 'Nome': nome, 'autor': autor, 'editora': editora}
    #Adcionando elementos pra lista_livro
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!\n")
    
#Função para exibir os livros de forma organizada      
def exibir_livro(livro):
    print('')
    print("ID:", livro['id'])
    print("Nome:", livro['Nome'])
    print("Autor:", livro['autor'])
    print("Editora:", livro['editora'])
    print('')
    
 #Função para consultar os livros   
def consultar_livro():
    #Estrutura de repetição
    while True:
        try:
            #Menu consultar livro
            print('-' * 51)
            print('-' * 14,'MENU CONSULTAR LIVRO', '-' * 15)
            #variável opcao chama função para verificar se o usúario digitou algum número válido
            opcao = input('Escolha a opção desejada: \n1 - Consultar Todos os Livros\n2 - Consultar Livro por ID\n3 - Consultar Livro(s) por autor\n4 - Retonar\n>>')
            print('')
            #if e elif sendo usado para verificar qual opção o usúario digitou e assim dar sua respectiva função
            if opcao == '1':
                for livro in lista_livro:
                    exibir_livro(livro)
            #Ao consultar um livro por ID o código verifica se o id informado esta cadastrado
            elif opcao == '2':
                id_global = int(input('Digite o id do livro: '))
                for livro in lista_livro:
                    if livro['id'] == id_global:
                        exibir_livro(livro)
                        break
                #Caso não estiver cadastrado o print é executado
                else:
                    print('\nLivro não encontrado.\n')
            #Consultando por nome do autor o código verificaa se o nome informado esta cadastrado
            elif opcao == '3':
                autor_livro = input('Digite o nome do autor:')
                for livro in lista_livro:
                    if livro['autor'] == autor_livro:
                        exibir_livro(livro)
                    #Caso não estiver cadastrado o print é executado
                    else:
                        print('\nLivro não encontrado\n')
            elif opcao == '4':
                break
            #Caso o usúario digitar um número ou caracter 
            else:
                print("Opção inválida\n")
        #Caso o usúario digitou algum número real ou caracter inválido e executado o print
        except ValueError:
            print('Digite um número inteiro\n')
 
#Função para remover o livro por ID            
def remover_livro():
    try:
        #Váriavel recebe o ID que o usúario deseja remover do cadastro
        id_global = int(input('Digite o id do livro: '))
        #Verifica se o ID informado pelo usúario esta cadastrado
        for livro in lista_livro:
            if livro['id'] == id_global:
                lista_livro.remove(livro)
                print('\nLivro removido com sucesso\n')
                break
        #Caso o ID informado não estiver cadastrado o print é executado
        else:
            print('Livro não encontrado.\n')
    #Caso o usúario digitou algum número real ou caracter inválido e executado o print
    except ValueError:
            print('Digite um número inteiro\n')
        
    
#Funçõo para verificar se o usúario digitou algum dos números informados
def escolha_servico(pergunta):
    opcoes = [1,2,3,4]
    while True:
        x = int(input(pergunta))
        if x in opcoes:
            return x
        #Caso o usúario digitou algum número que não esta na lista e executado o print
        else:
            print('Escolha inválida, tente novamente\n')

#Programa principal
while True:
    try:
        #Menu principal
        print('-' * 50)
        print('-' * 17,'MENU PRINCIPAL', '-' * 17)
        
        #variável op chama função para verificar se o usúario digitou algum número válido
        op = escolha_servico('Escolha a opção desejada: \n1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair\n>>')
        #if e elif sendo usado para verificar qual opção o usúario digitou e assim dar sua respectiva função
        if op == 1:
            cadastrar_livro()
        elif op == 2:
            consultar_livro()
        elif op == 3:
            remover_livro()
        elif op == 4:
            print("Encerrando o programa...")
            break
    #Caso o usúario digitou algum número real ou caracter inválido e executado o print
    except ValueError:
            print('Digite um número inteiro\n')

        