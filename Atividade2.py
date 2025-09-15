# Lista para armazenar os números
lista_numeros = []

# Loop para coletar 10 números do usuário
print("Digite 10 números, sendo um deles o seu número da chamada.")
i = 0
while i < 10:
    try:
        numero = int(input(f"Digite o {i+1}º número: "))
        lista_numeros.append(numero)
        i += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# --- Exibição das listas ---

print("\n--- Resultados ---")

# 1. Lista original
print(f"Lista original: {lista_numeros}")

# 2. Lista ordenada crescente
lista_ordenada = sorted(lista_numeros)
print(f"Lista ordenada crescente: {lista_ordenada}")

# 3. Lista sem números repetidos
# A melhor maneira de remover duplicatas é convertendo a lista para um 'set'
# e depois convertendo de volta para uma lista.
lista_sem_repetidos = list(set(lista_numeros))
# É bom ordenar a lista sem repetidos para que ela seja mais fácil de ler
lista_sem_repetidos.sort()
print(f"Lista sem números repetidos: {lista_sem_repetidos}")
