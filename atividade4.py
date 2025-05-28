numeros = list(range(1, 101))
print(numeros)

for num in numeros:
    if num % 2 == 0:
        print(num, "Número Par")
    if num > 1:  
        primo = True
        for i in range(2, int(num**0.5) + 1): 
            if num % i == 0:  
                primo = False
                break
        if primo:  
            print(num, "Número Primo")
