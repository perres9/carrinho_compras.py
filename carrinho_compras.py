# Sistema de Carrinho de Compras
# Entrada: Lista de produtos com nome e preço
# Saída: Lista formatada dos produtos e total da compra

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# Exibe os itens no formato pedido
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

# Exibe o total no formato pedido
print(f"Total: R${total:.2f}")
