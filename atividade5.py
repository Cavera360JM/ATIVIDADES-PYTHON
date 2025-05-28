class Usuario:
    def __init__(self, nome1, nome2, nome3, nome4, nome5, nome6, nome7, nome8, nome9, nome10):
        self.nomes = [nome1, nome2, nome3, nome4, nome5, nome6, nome7, nome8, nome9, nome10]

    def verificar_nome(self):
        for nome in self.nomes:
            if not nome.replace(" ", "").isalpha():
                raise ValueError(f"O nome '{nome}' contém caracteres inválidos.")
    def organizar_e_contar(self):
        self.nomes.sort()
        for nome in self.nomes:
            print(f"Nome: {nome} - Quantidade de letras: {len(nome.replace(' ', ''))}") 
def main():
    print("--- Cadastro de Usuário ---")
    nome1 = input("Digite seu nome1: ")
    nome2 = input("Digite seu nome2: ")
    nome3 = input("Digite seu nome3: ")
    nome4 = input("Digite seu nome4: ")
    nome5 = input("Digite seu nome5: ")
    nome6 = input("Digite seu nome6: ")
    nome7 = input("Digite seu nome7: ")
    nome8 = input("Digite seu nome8: ")
    nome9 = input("Digite seu nome9: ")
    nome10 = input("Digite seu nome10: ")
    try:
        usuario = Usuario(nome1, nome2, nome3, nome4, nome5, nome6, nome7, nome8, nome9, nome10)
        usuario.verificar_nome()
        usuario.organizar_e_contar()
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()
