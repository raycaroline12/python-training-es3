# Script para saber múltiplos de um número utilizando o comando for

numero = int(input("Digite um número para saber os seus múltiplos: "))
total = int(input("Informe um número máximo para a taboada: "))

for cont in range(0, total + 1, numero):                     # O passo é definido pelo 1º número digitado pelo usuário
    print(numero, "x", cont // numero, " = ", cont)          # Print para definir o layout
