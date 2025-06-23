aniversario = 4  
controle = 0

while controle <= 100:
    multiplicacao = controle * aniversario
    controle += 1
    if multiplicacao > 1000:
        print(f"O número {multiplicacao} é maior que 1000")
    print(multiplicacao)
