#Script parecido com o example_if, mas utilizando o comando elif.

nota1 = float(input('Digite a nota 1 do aluno: ')) #Recebe a nota e converte a string em um número do tipo float
nota2 = float(input('Digite a nota 2 do aluno: '))
media = (nota1+nota2)/2                          # Calcula a média

if media >= 7:
    print('Aluno aprovado com média: ', media)
elif media >= 4:                                 #O elif substitui o else if
    print('O aluno fará final pois ficou com média: ', media)
else:
    print('Aluno reprovado com média: ', media)