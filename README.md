![Header](./img/HEADER.png)

# Step by Step through Python

> Concentramos nesse espaço um resumo de tudo o que você precisa saber sobre  a linguagem de programação Python antes de começar a trabalhar. Não pule esta estapa, ela é imprescindível para que o seu desenvolvimento e avanço no projeto seja mais rápido.


[![Read the docs][docs-image]][docs-url]
> O conteúdo deste passo a passo é resumido. Dúvidas surgirão ao longo do desenvolvimento. Para saná-las, leia a documentação! Ela é completa!
> * Link: https://docs.python.org/3/
---
# Let's go!

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Sumário</summary>
  <ol>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#execution">Execution</a></li>
      </ul>
    </li>
    <li><a href="#primeiro-programa">Primeiro programa</a></li>
    <li><a href="#condicionais">Condicionais</a></li>
    <li><a href="#loops">Loops</a></li>
    <li><a href="#funcoes">Funções</a></li>
    <li><a href="#classes">Classes</a></li>
    <li><a href="#bibliotecas">Bibliotecas</a></li>
  </ol>
</details>

<!--**Your name**
* *Initial work* - [repository-name][repository-url] (Repository space)
* *Released on* [cloud-provider][cloud-provider-url] (Cloud provider)
* *My professional profile on* [LinkedIn][linkedin-url]-->
---


# Getting started

Para iniciar, é necessário verificar se o Python está instalado no seu sistema operacional. Você precisa também entender como executar um programa em Python. Separamos estes tópicos em duas sessões apresentadas a seguir.

<!--_For more examples and usage, please refer to the [Wiki][wiki]._-->


## Installation

O Python já	vem	instalado nos sistemas Linux e Mac OS, mas será	necessário
fazer o	download da **versão 3.9**, que é a utilizada no projeto. O Python não vem instalado por padrão no Windows e o download deverá ser feito no site https://www.python.org/downloads/.


**Update da versão 3.9 em Linux:**

*Verificar a versão atual:*

```sh
$ python3 --version
```
*Instalar a versão 3.9 (caso a atual não seja esta):*
```sh
$ sudo apt update -y
$ sudo apt install python3.9
```

## Execution

### Modo Interativo

Para executar um programa em Python, pode-se acessar o Shell do Python, chamado de Python Interativo ou de Python Shell, usando o comando **python** no terminal. Os comandos são executados imediatamente quando se pressiona a tecla enter. Neste caso, não é possível estruturar códigos e procedimentos mais complexos. Ele é melhor utilizado para testes de procedimentos simples e instruções rápidas. Para sair e voltar ao terminal, deve-se usar o comando **exit()**.

```
$ python
Python 3.9.2 (default, Oct  8 2020, 12:12:24)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Olá")
Olá
>>> exit()
$
```
### Modo Script

Como citado, o modo Interativo não é capaz de armazenar sequências de comandos ou rotinas para serem executados posteriormente. Para isso, é preciso usar códigos, conhecidos como roteiros ou scripts, no caso do Python, chamado de Python Script.
Esses arquivos contém instruções para serem executadas. É importante afirmar novamente que os scripts são executados de formas sequenciais. Eles podem ser criados até mesmo pelo bloco de notas ou qualquer editor de texto e editados livremente. Para isso, basta salvá-los com a extensão .py.

Para executá-los, basta abrir o terminal, navegar até onde estão salvos os arquivos desejados e usar o comando python arquivo.py:

```
# Certifique-se de que o arquivo
# esteja no diretorio corrente
$ python meu_programa.py
```

---

# Primeiro programa

![Img2](./img/python.png)

## Entrada do usuário

## Comando print


---

# Condicionais

* [Maven](https://maven.apache.org/) - Dependency Management
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) - To deploy on Heroku

<!--## Release History

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Refactoring - Remove `setAnyMethod()`
    * ADD: Add `newSomething()`
* 0.1.1
    * FIX: Crash when calling `defaultXYZ()` (Thanks @ContributorName)
* 0.1.0
    * The first proper release
* 0.0.1
    * Initial work -->

---

# Loops

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

---

# Funções

Um dos conceitos mais importantes em programação é o de função. As funções tornam possível decompor um programa complexo em uma série de sub-rotinas mais simples, que por sua vez podem ser divididas em fragmentos menores, e assim por diante. Por outro lado, as funções são reutilizáveis: se tivermos uma função capaz de calcular uma raiz quadrada, por exemplo, podemos usá-la em todos os lugares em nossos programas sem precisar reescrevê-la todas as vezes.


## A função print()

Já conhecemos essa função, mas cabe especificar que a função print() pode exibir qualquer número de valores fornecidos como argumentos (isto é, entre parênteses). Por padrão, esses valores serão apresentados separados uns dos outros por um espaço e por fim será adicionada uma quebra de linha. Você pode substituir o separador padrão (espaço) por qualquer outro caractere (ou mesmo qualquer caractere) com o argumento sep. Exemplo:

```python
>>> print("Bom", "dia", "a", "todos", sep ="*")
Bom*dia*a*todos
>>> print("Bom", "dia", "a", "todos", sep ="")
Bomdiaatodos
```

Da mesma forma, você pode substituir a quebra de linha pelo argumento final:

```python
>>> n =0
>>> while n<6:
...     print("zut", end ="")
...     n = n+1
...
zutzutzutzutzut
```

## Importar um módulo de funções

Você já encontrou algumas funções embutidas no próprio Python, como a função `len()`, que retorna o tamanho de uma string ou de uma lista. As funções integradas na linguagem são relativamente poucas: são apenas aquelas que provavelmente serão usadas com muita frequência. Os outros são agrupados em arquivos separados chamados módulos.

Veremos como é fácil dividir um programa mais complicado em vários arquivos pequenos para facilitar a manutenção. Um aplicativo típico do Python consistirá, então, em um programa principal, acompanhado por um ou mais módulos, cada um contendo as definições de várias funções complementares. Há um grande número de módulos pré-programados que são automaticamente fornecidos com o Python. Muitas vezes são agrupados em um único módulo conjuntos de funções relacionadas, que chamamos de bibliotecas. O módulo de matemática, por exemplo, contém definições de muitas funções matemáticas, como seno, cosseno, tangente, raiz quadrada e assim por diante. Para poder usar essas funções, basta incorporar a seguinte linha no início do script:

```python
from math import *
```

Esta linha diz ao Python que ele deve incluir no programa atual todas as funções (este é o significado do asterisco) do módulo de matemática, que contém uma biblioteca de funções matemáticas pré-programadas.

No corpo do próprio script, você escreverá por exemplo: raiz = sqrt(numero) para atribuir à variável raiz a raiz quadrada do número, seno_x = sin(angulo) para atribuir à variável seno_x o seno do ângulo (em radianos!), etc.

Exemplo:

```python
# Demo: usando as funções do módulo <math>

from math import *

numero = 121
angulo = pi/6        # é 30°
                    # (a biblioteca de matemática também inclui a definição de pi)
print("raiz quadrada de", numero, "=", sqrt(numero))
print("seno de", angulo, "radianos", "=", sin (angulo))
```

Executar este script faz com que a exibição a seguir:

```
raiz quadrada de 121 = 11.0
seno de 0.5235987755982988 radianos = 0.49999999999999994
```

## Definindo funções

A programação é a arte de ensinar ao computador como executar tarefas que ele não era capaz de fazer. Um dos métodos mais interessantes para isso é adicionar novas instruções na forma de funções originais.

A abordagem eficaz para um problema complexo, tipicamente, consiste de dividi-lo em subproblemas mais simples, que serão estudados separadamente. Por outro lado, muitas vezes a mesma sequência de instruções deve ser usada várias vezes em um programa, e obviamente não será necessária reproduzi-la repetidamente.

A sintaxe do Python para definir uma função é a seguinte:

```python
def nomedafuncao(argumento1, argumento2, ...):
     bloco de código
```

* Você pode escolher qualquer nome para a função que está criando, com exceção das palavras reservadas pela língua e desde que você não use nenhum caractere especial ou acentuado (o caractere underline `_` é permitido). Como é o caso dos nomes de variáveis, aconselha-se a usar principalmente letras minúsculas, especialmente no início do nome.
* Como as declarações `if` e `while` que você já conhece, a instrução `def` é uma instrução composta. A linha que contém esta instrução termina necessariamente com dois pontos, que introduz um bloco de código que você não deve esquecer de indentar.
* A lista de parâmetros especifica quais informações fornecer como argumentos quando você quiser usar esta função (parênteses podem permanecer vazios se a função não requer argumentos).
* Uma função é usada quase como qualquer instrução. No corpo de um programa, chamar uma função consiste do nome da função seguido de parênteses. Se necessário, deve-se colocar o argumento ou argumentos que queremos transmitir para a função dentro dos parênteses.

### Função Simples sem parâmetros

```python
>>> def tabuada7():
...     n = 1
...     while n <11 :
...         print(n * 7, end =' ')
...         n = n +1
...
```

Depois de definir a função acima, podemos executá-la:

```python
>>> tabuada7()
```

E observaremos

```python
7 14 21 28 35 42 49 56 63 70
```

Agora podemos reutilizar esse recurso várias vezes, quantas vezes desejarmos. Podemos também incorporá-lo na definição de outra função, como no exemplo abaixo:

```python
>>> def tabuada7tripla():
...     print('A tuabuada do 7 triplicada:')
...     tabuada7()
...     tabuada7()
...     tabuada7()
...
```

Quando executada

```python
>>> tabuada7tripla()
A tuabuada do 7 triplicada:
7 14 21 28 35 42 49 56 63 70
7 14 21 28 35 42 49 56 63 70
7 14 21 28 35 42 49 56 63 70
```

### Função com parâmetros

Não seria mais interessante definir uma função que possa exibir qualquer tabuada, sob demanda?

Na definição de tal função, é necessário fornecer uma variável específica para receber o argumento transmitido. Essa variável específica é chamada de parâmetro. Esse parâmetro recebe um nome com as mesmas regras de sintaxe das variáveis (sem letras acentuadas, etc.) e esse nome é colocado entre os parênteses que acompanham a definição da função. Aqui está o que nos interessa:

```python
>>> def tabuada(base):
...    n = 1
...    while n <11 :
...       print(n * base, end =' ')
...
```

Experimente:

```python
>>> tabuada(13)
13 26 39 52 65 78 91 104 117 130
```

```python
>>> tabuada(9)
9 18 27 36 45 54 63 72 81 90
```

Utilizando uma variável como um argumento

O argumento que usamos ao chamar uma função também pode ser uma variável, como no exemplo abaixo. Dê uma boa olhada e execute este exemplo. Este exemplo apresenta um caso da utilidade das funções simples para realizar tarefas complexas.

```python
>>> a = 1
... while a <20:
...    tabuada(a)
...    print("")
...    a = a + 1
...
```

> Nota importante

No exemplo acima, o argumento que passamos para a função tabuada() é o conteúdo da variável a. Dentro da função, esse argumento é atribuído ao parâmetro base, que é uma variável totalmente diferente. Então observe agora que:

> O nome de uma variável que passamos como argumento de uma função não tem relação com o nome do parâmetro correspondente na função.

Esses nomes podem ser idênticos, mas é importante entender que eles não designam a mesma coisa (apesar do fato de que eles podem conter o mesmo valor).

### Funções com vários parâmetros

A função `tabuada()` é certamente interessante, mas sempre exibe apenas os dez primeiros termos da tabela de multiplicação, ao passo que podemos desejar que ela exiba outros. Não importa. Vamos aprimorá-lo adicionando parâmetros adicionais, em uma nova versão que chamaremos a essa tabela de `tabuadaMulti()`:

```python
>>> def tabuadaMulti(base, inicio, fim):
...    print('Parte da tabuada da base', base, ':')
...    n = inicio
...    while n <= fim :
...       print(n, 'x', base, '=', n * base)
...       n = n +1
```

Esta nova função, portanto, usa três parâmetros: a base da tabela como no exemplo anterior, o índice do primeiro termo a ser exibido, o índice do último termo a ser exibido. Experimente.

### Variáveis ​​locais, variáveis ​​globais

Quando definimos variáveis ​​dentro do corpo de uma função, essas variáveis ​​são acessíveis apenas à própria função. Essas variáveis ​​são consideradas variáveis ​​locais para a função. Isto é, por exemplo, o caso das variáveis `​​base`, `inicio`, `fim` e `n` no exercício anterior. Se tentarmos exibir o conteúdo da variável base logo após realizar o exercício acima, receberemos uma mensagem de erro:

```python
>>> print(base)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'base' is not defined
```

A máquina nos diz claramente que o símbolo base é desconhecido. Variáveis ​​definidas fora de uma função são variáveis ​​globais. Seu conteúdo é “visível” de dentro de uma função, mas a função não pode mudá-la. exemplo:

```python
>>> def mask():
...     p = 20
...     print(p, q)
...
>>> p, q = 15, 38
>>> mask()
20 38
>>> print(p, q)
15 38
```

### Funções e procedimentos

Para os puristas, as funções que descrevemos até agora não são exatamente funções no sentido estrito, mas sim procedimentos. Uma função “verdadeira” (no sentido exato) deve, de fato, retornar um valor quando termina. É isso que acontece quando utilizamos` y = sin(a)`, por exemplo. É fácil entender que nesta expressão, a função `sin()` retorna um valor (o seno do argumento `a`) que é então atribuído à variável `y`.

Vamos começar com um exemplo simples:

```python
>>> def cubo(w):
...    return w*w*w
...
```

A instrução `return` define o valor devolvido pela função. Neste caso será o argumento que foi passado para a função elevado ao cubo. Exemplo:

```python
>>> b = cubo(9)
>>> print(b)
729
```

Após aprender estes tópicos sobre funções, você será capaz de modularizar seu código, trazendo legibilidade e facilidade para dar manutenção do mesmo.

Segue uma dica sobre o uso de funções/módulos:

> * É mais fácil testar os módulos individualmente do que o programa completo.
# Classes

---

# Bibliotecas

<!-- Markdown link & img dfn's -->


[repository-url]: https://github.com/alexandrerosseto/wbshopping

[cloud-provider-url]: https://wbshopping.herokuapp.com

[linkedin-url]: https://www.linkedin.com/in/alexandrerosseto

[wiki]: https://github.com/yourname/yourproject/wiki

[docs-image]: https://img.shields.io/badge/IMPORTANT-READ%20THE%20DOCS!-blue
[docs-url]: https://docs.python.org/3/
[Frontend-image]: https://img.shields.io/badge/Frontend-Ionic-blue?style=for-the-badge
[Frontend-url]: https://img.shields.io/badge/Frontend-Ionic-blue?style=for-the-badge
[Backend-image]: https://img.shields.io/badge/Backend-Java%208-important?style=for-the-badge
[Backend-url]: https://img.shields.io/badge/Backend-Java%208-important?style=for-the-badge
