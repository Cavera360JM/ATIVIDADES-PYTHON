import random
import string

def gerar_senha_personalizada(nome):
  """
  Gera uma senha aleatória de 20 caracteres com o nome no meio.
  """
  # Conjunto de caracteres para a senha
  caracteres = string.ascii_letters + string.digits + string.punctuation
  
  # Nome a ser inserido na senha
  nome_completo = nome.replace(" ", "") # Remove espaços do nome, se houver
  tamanho_nome = len(nome_completo)
  
  # A senha terá 20 caracteres, então precisamos de 20 - tamanho_nome de caracteres aleatórios.
  tamanho_aleatorio = 20 - tamanho_nome
  
  # Posição do meio para inserir o nome. Usamos a divisão inteira (//) para garantir um número inteiro.
  meio = tamanho_aleatorio // 2
  
  # Gera a primeira parte da senha aleatória
  parte1 = ''.join(random.choice(caracteres) for _ in range(meio))
  
  # Gera a segunda parte da senha aleatória
  # A segunda parte pode ser ligeiramente maior se o tamanho_aleatorio for ímpar
  parte2 = ''.join(random.choice(caracteres) for _ in range(tamanho_aleatorio - meio))
  
  # Junta tudo: parte1 + nome + parte2
  senha_final = parte1 + nome_completo + parte2
  
  return senha_final

# Meu nome para ser inserido na senha
nome = "João Miguel"

# Chamar a função para gerar a senha e mostrar o resultado
senha_gerada = gerar_senha_personalizada(nome)

print(f"A sua nova senha é: {senha_gerada}")
