import sys

print("Saiba quantos dos valores digitados são positivos e qual e sua media")
numeroLista = []
media = []
numeropositivos = 0
for i in range(1 , 7):
    numero = int(input(f"Digite o {i}° numero:"))
    numeroLista.append(numero)
    if numero > 0 :
         media.append(numero)
         numeropositivos = numeropositivos + 1
if not any(I > 0 for I in numeroLista):
    print("pelo menos 1 dos numeros deve ser positivo")
    sys.exit()

somamed = sum(media)
nummed = len(media)

med = somamed/nummed

print(f"{numeropositivos} valores positivos")
print(f"{med:.1f}")