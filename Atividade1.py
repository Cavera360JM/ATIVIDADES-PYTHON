import collections
import re

def analisar_texto():
  """
  Pede um texto ao usuário e analisa.
  """
  texto = input("Digite o texto que você quer analisar: ")
  
  if not texto.strip():
    print("Você não digitou nada.")
    return

  # Usei a expressão regular para encontrar as palavras e garantir que a pontuação não interfira.
  palavras = re.findall(r'\b\w+\b', texto.lower())
  
  # Contagem total de palavras
  contagem_total = len(palavras)
  
  # A palavra mais longa
  if palavras:
    palavra_mais_longa = max(palavras, key=len)
  else:
    palavra_mais_longa = "N/A"
  
  # A palavra que mais aparece
  if palavras:
    contador = collections.Counter(palavras)
    palavra_mais_frequente = contador.most_common(1)[0][0]
  else:
    palavra_mais_frequente = "N/A"
  
  print("\n--- Análise do Texto ---")
  print(f"Número total de palavras: {contagem_total}")
  print(f"A palavra mais longa é: '{palavra_mais_longa}'")
  print(f"A palavra que mais aparece é: '{palavra_mais_frequente}'")

# Para rodar o programa, chame a função
analisar_texto()
