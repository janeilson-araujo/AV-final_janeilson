print("saiba qual o aumento do seu salario")
salario = float(input("digite seu salario:")) #Apresentamos o programa e pedimos o salario

if salario >= 0.00 and salario <= 400.00:
    porcentagem15 = (salario * 0.15)
    aumento15 =  porcentagem15 + salario
    print(f"Novo salario: {aumento15:.2f}")
    print(f"Reajuste ganho: {porcentagem15:.2f}")
    print("Em percentual: 15 %")
elif salario >= 400.01 and salario <= 800.00:
    porcentagem12 = (salario * 0.12)
    aumento12 =  porcentagem12 + salario
    print(f"Novo salario: {aumento12:.2f}")
    print(f"Reajuste ganho: {porcentagem12:.2f}")
    print(f"Em percentual: 12 %")
elif salario >= 800.01 and salario <= 1200.00:
    porcentagem10 = (salario * 0.10)
    aumento10 =  porcentagem10 + salario
    print(f"Novo salario: {aumento10:.2f}")
    print(f"Reajuste ganho: {porcentagem10:.2f}")
    print(f"Em percentual: 10 %")
elif salario >= 1200.01 and salario <= 2000.00:
    porcentagem7 = (salario * 0.07)
    aumento7 =  porcentagem7 + salario
    print(f"Novo salario: {aumento7:.2f}")
    print(f"Reajuste ganho: {porcentagem7:.2f}")
    print(f"Em percentual: 7 %")
elif salario > 2000.00:
    porcentagem4 = (salario * 0.04)
    aumento4 =  porcentagem4 + salario
    print(f"Novo salario: {aumento4:.2f}")
    print(f"Reajuste ganho: {porcentagem4:.2f}")
    print(f"Em percentual: 4 %")