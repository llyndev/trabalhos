#Trabalho basico para um app de vendas aplicando descontos

#Mensagem de boas-vindas
print('Bem-vindo a loja do Weslley Alves')

# Recebendo o valor unitário e a quantidade do produto do usuário
produto = int(input('Entre com o valor do produto: '))
qtd = int(input('Entre com a quantidade do produto: '))

# Calculando o valor total sem desconto
total = produto * qtd

# Verificando o desconto com base no valor total
if total < 2500:
    desconto = total
    
elif total >= 2500:
    if total < 6000:
        desconto = total - (total * 4 / 100) # Calculando o valor total com desconto
        
    elif total >= 6000:
        if total < 10000:
            desconto = total - (total * 7 / 100) # Calculando o valor total com desconto
        else:
            total >= 10000
            desconto = total - (total * 11 / 100) # Calculando o valor total com desconto
            
# Exibindo os resultados
print(f'O valor SEM desconto R${total:.2f}\nO valor COM desconto R${desconto:.2f}')
    
    