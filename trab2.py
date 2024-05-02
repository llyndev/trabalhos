#Mensagem de boas-vindas
print('-Bem-vindo a Loja de Gelados do Weslley Alves-')
print('-' * 18, 'Cardápio', '-' * 18)
print('-' * 46)
print('-' * 3, '|', 'Tamanho', '|', 'Cupuaçu (CP)', '|', 'Acaí (AC)', '|', '-' * 3 )
print('-' * 3, '|' ,'   P   ','|', '   R$ 9.00  ', '|', ' R$ 11.00', '|', '-' * 3 )
print('-' * 3, '|' ,'   M   ','|', '   R$ 14.00 ', '|', ' R$ 16.00', '|', '-' * 3 )
print('-' * 3, '|' ,'   G   ','|', '   R$ 18.00 ', '|', ' R$ 20.00', '|', '-' * 3 )
print('-' * 46)

#Variavel do valor total a ser pago
total = 0 

#Estrutura de repetição com loop infinito 
while True:
    
    #Recebe o sabor desejado do cliente
    sabor = input('Entre com o sabor desejado (CP/AC): ').upper()  
        
    #Verifica se o sabor esta incluso, caso não estiver executa o print e retorna ao inicio
    if sabor not in ['CP', 'AC']:
        print('Sabor inválido. Tente novamente\n')
        continue
        
    #Recebe o tamanho desejado do cliente
    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
        
    #Verifica se o tamanho  esta incluso, caso não estiver executa o print e retorna ao inicio
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente\n')
        continue
        
    #Verifica qual sabor foi escolhido
    if sabor == 'CP':
        #Verifica o tamanho solicitado e o total recebe a soma 
        if tamanho == 'P':
            total += 9
        elif tamanho == 'M':
            total += 14
        elif tamanho == 'G':
            total += 18
        print(f'Você pediu um Cupuaçu no tamanho {tamanho}: R${total}\n')
                                            
    if sabor == 'AC':  
        if tamanho == 'P':
            total += 11
        elif tamanho == 'M':
            total += 16
        elif tamanho == 'G':
            total += 20
        print(f'Você pediu um Açaí no tamanho {tamanho}: R${total}\n')
     
    #Print perguntando se o usuario deseja algo a mais
    continuar = input('Deseja mais alguma coisa? (S/N): ').upper()
    
    #Verifica a escolha se 'S' retorna ao inicio se 'N' fecha o programa
    if continuar == 'S':
        continue
    else:
        break
    
#Ao escolher 'N' e mostrado o valor total a ser pago
print(f'O valor total a ser pago: R${total}')
                

                
                
