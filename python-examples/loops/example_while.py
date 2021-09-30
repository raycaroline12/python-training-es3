# Script para calcular a média de valores fornecidos pelo usuário utilizando o comando while.
aux = 0  # váriavel auxiliar para verificar a condição do loop
cont = -1  # contador para a divisão da média
soma = 0  # soma os valores digitados

while aux >= 0:  # caso o usuário digite um valor negativo, o loop se encerra o  programa segue seu fluxo
    soma += aux
    cont += 1
    aux = float(input("Digite números, para sair digite qualquer valor negativo:"))

if cont == 0:  # if para impedir a divisão por 0
    cont = 1

print("A média dos valores digitados é: ", soma / cont)