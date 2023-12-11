print("saiba quantos valores pares existem entre 5 numeros")
numpares = 0#a variavel numpares armazena a quantidade de numeros pares
for i in range(5):#o for é utilizado para perguntar os 5 numeros 
    numeros = int(input("digite os numeros:"))
    if numeros % 2 == 0 :#o if analisa de os numeros são pares ou inpares
        numpares = pares + 1 #se o numero for par é adicionado +1 a numpares
print(f"{numpares} valores pares")#exibimos a quantidade de numeros pares