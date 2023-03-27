# **ExDNS**
![Bower](https://img.shields.io/bower/l/bootstrap)
![GitHub file size in bytes](https://img.shields.io/github/size/jhonimenezes/dnsexpl0rer/ExpD.py)

# Dependências

- [Python](https://www.python.org/downloads/)

# Introdução
 
O programa desenvolvido em Python foi desenvolvido para realizar a principal tarefa: verificar se uma lista de diretórios ocultas especificadas por uma wordlist existe ou não. Por padrão a wordlist é a mesma utilizada no Dirb.

Dessa forma, o programa oferece uma maneira simples e prática de obter informações  DNS de um host para verificar a existência de diretórios em uma lista especificada em um arquivo padrão ou **CRIADA** pelo usuário.

# Instalação

Para instalar o ExDNS basta clonar o repositório do github:

```bash
$ git clone https://github.com/jhonimenezes/ExpD

```

Em seguida entre na pasta do projeto:

```bash
$ cd dnsexplorer
```

# Execução

Para executar o programa basta digitar:

```bash
$ python3 ExDNS.py

```

Quando solicitado informe o nome do host que deseja verificar


<img src="https://raw.githubusercontent.com/jhonimenezes/img/main/execucaoprograma.png?token=GHSAT0AAAAAACAFWSG3F2RLM4KRPVCSXUECZBBXCAQ"></img>

<!--![Imagem execução](https://github.com/jhonimenezes/img/blob/main/execucaoprograma.png)-->

Em seguida será solicitado o nome da wordlist

> por padrão a wordlist é a mesma usada no Dirb

Caso queira utilizar outra wordlist de sua preferencia basta salvar dentro do diretório e informar o nome ao programa.

Ex:

```bash
Digite o nome da wordlist: wordlistEdit.txt

```

#### Observação:
Caso o arquvo esteja sem a extenção visível, digite o nome sem a extenção. ex:

> ***wordlist***

> Digite o nome da Wordlist:            ***wordlist***

ou

> ***wordlist.txt***
>
> Digite o nome da wordlist: ***wordlist.txt***

O programa exibirá um load enquanto faz a verificação de cada um dos diretórios listados da wordlist existe ou não. O resultado será exibido na tela.

Caso queira interromper a execução do programa utilize o atalho:

`ctrl + c`

# Conclusão

Certifique-se  de que você tenha permissão para executar o programa em seu computador. Não esqueça de que é importante que a wordlist esteja na mesma pasta do programa para que o programa possa lê-lo corretamente.

O Tempo de execução do programa pode variar de acordo com o tamanho da lista.
