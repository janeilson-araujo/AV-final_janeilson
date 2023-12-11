ddd = int(input("digite o DDD: "))
#pedimos ao usuario algum DDD
cidadesDDD = {61 : "Brasilia" , 71 : "Salvador" , 11 : "Sao Paulo" , 21 : "Rio de Janeiro" , 32 : "Juiz de Fora" , 19 : "Campinas" , 27 : "Vitoria" , 31 : "Belo Horizonte"}
# o dicionario cidadesDDD armazena os DDDs cadastrados
while ddd not in cidadesDDD:
    print("DDD não cadastrado")
    ddd = int(input("digite o DDD :"))
#enquanto o ddd inserido pelo ususrio não estiver em cidadesDDD ele pedira o DDD novamente
print(cidadesDDD[ddd])
#caso o DDD inserido pelo ususrio estiver em cidadesDDD a cidade pertencente ao DDD sera exibida