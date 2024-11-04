# Ler uma lista de 10 números reais e mostre-os na ordem inversa.

numeros = [float(input(f"digite o número {i + 1}: "))
            for i in range(0, 10)]

lista = numeros
lista.reverse()

print(lista)