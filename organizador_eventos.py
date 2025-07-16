# Organizador de Eventos por Tema
# Entrada: Lista de participantes com seus respectivos temas
# Saída: Dicionário com os temas como chave e os nomes agrupados

# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# Loop para armazenar participantes e seus temas
for _ in range(n):
    linha = input().strip()
    nome, tema = linha.split(", ")
    
    if tema not in eventos:
        eventos[tema] = []
    
    eventos[tema].append(nome)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
