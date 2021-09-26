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

---

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
