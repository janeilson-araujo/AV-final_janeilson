print("calcule seu imposto de renda") 
salario = float(input("digite o seu salario:")) #pedimos para o usuario inserir seu salario

if salario <= 2000.00:
   print("Isento") # calculamos se o salario do usuario é menor que 2000.00 se sim a saida sera isento
elif salario >= 2000.01 and salario <= 3000.00:
   porcentagem8 = salario * 0.08 
   print(f"R$ {porcentagem8:.2f}") # calculamos se o salrio esta entre 2000.01 e 3000.00 se sim a saida sera 8% do valor de entrada 
elif salario >= 3000.01 and salario <= 4500.01:
    porcentagem18 = salario * 0.18 # calculamos se o salrio esta entre 3000.01 e 4500.00 se sim a saida sera 18% do valor de entrada 
    print(f"R$ {porcentagem18:.2f}")
elif salario > 4500.00:
    porcentagem28 = salario * 0.28 # calculamos se o salrio esta acima de 4500.00 se sim a saida sera de 28% do valor de entrada
    print(f"R$ {porcentagem28:.2f}")