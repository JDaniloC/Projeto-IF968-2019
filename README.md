# TODO.TXT - Projeto IF968, CIn UFPE
<p align="center">
<image src="http://todotxt.org/images/todotxt_logo_2012.png">
</p>

> Um Shell Script simples para admnistração de seu arquivo todo.txt.

>> "O objetivo deste trabalho é praticar a escrita de funções e programas em Python, em particular, programas envolvendo strings, ~~vetores~~, listas, tuplas, dicionários e arquivos. Além disso, é a primeira oportunidade que os alunos têm, no contexto do curso de *Sistemas de Informação*, de desenvolver um sistema não-trivial, ainda que simples." ~[Fernando Castor](https://sites.google.com/a/cin.ufpe.br/castor/).

*Leia sobre o [projeto](https://docs.google.com/a/cin.ufpe.br/viewer?a=v&pid=sites&srcid=Y2luLnVmcGUuYnJ8aWY5NjhzaXxneDozNzU3OWRjNDFiZjdiNTAz) para saber o desenvolvimento.*

<p float="left">
  <image width=49%, src="./add.gif"/> 
  <image width=49%, src="./list.gif"/>
</p>

## Obtenção do Script

### Download
Download direto pelo botão verde **Clone or Download** ou abra o VSCode, pressione Ctrl+Shift+P e digite *"Git clone"* e cole *https://github.com/Tiodonilo/Projeto-IF968-2019.git* para salvar em um repositório local.

### Instruções e Comandos

```shell
# Abra o Shell: CMD/Bash... Dentro do repositório local.
# Tente Python, Python3 ou py dependendo da versão e configuração do python!
# Para testar abra o Prompt de comando e digite python se abrir o 2.6 ou dar erro, então tente python3.
# Se der erro de syntax ou quaisquer outras circunstâncias, tente py ou verifique se o python está no path.
```

#### Comandos

> Comando adicionar: a

```shell
>> python agenda.py a (data) (hora) (prioridade) (descrição) (contexto) (projeto)
```
*NOTA:* Sempre nessa ordem, a única informação obrigatória é a descrição, que é a informação da tarefa.

- `Data`: A data referente a criação ou objetivo da tarefa, pode ser referenciado no comando Listar.
  - Formato 1: **DDMMAAAA**, sem espaço, apenas números.
  - Formato 2: **"ontem"** ou **"hoje"** ou **"amanhã"**, sempre minúsculo, sem aspas.
- `Hora`: A hora referente a criação ou objetivo da tarefa, pode ser referenciado no comando Listar.
  - Formato 1: **HHMM,** sem espaço, apenas números.
  - Formato 2: **"agora",** sempre minúsculo, sem aspas.
- `Prioridade`: Quão importante é a tarefa, podem ser referenciados e serão anexados no início do comando Listar.
  - Formato 1: **(A) - (Z)**, com ou sem parênteses.
  - Formato 2: **(a) - (z)**, com ou sem parênteses.
- `Contexto`: Contexto da tarefa para ser referenciado depois no comando Listar, formato: **@Contexto**.
- `Projeto`: Projeto relacionado à tarefa, para ser referenciado no comando Listar, formato: **+Projeto**.

> Comando listar: l

```shell
>> python agenda.py l (data, hora, prioridade, contexto ou projeto, opcional.)
```
*NOTA:* Comando L, sempre minúsculo. Quando sozinho irá listar todos os itens do arquivo todo.txt

###### Serão usados os mesmos formatos do comando adicionar, se o contexto/projeto estiver sem o sinal, aparecerá ambos.

> Comando remover: r

```shell
>> python agenda.py r (index da tarefa)
```
###### Irá remover a tarefa do todo.txt, pode vários indices separados por espaço, números inteiros, sem parênteses.

> Comando fazer: f

```shell
>> python agenda.py f (index da tarefa)
```
###### Irá retirar a tarefa do todo.txt e move-lo para o done.txt. Mesmas regras do comando R.

> Comando prioridade: p

```shell
>> python agenda.py p (prioridade) (indice da tarefa)
```
###### Irá adicionar ou alterar a prioridade de uma determinada tarefa. Mesmas regras do comando R e A.

> Comando help: h

```shell
>> python agenda.py h
```
###### Irá mostrar o formato do comando A. Não recebe parâmetros.

> Comando interface: i

```shell
>> python agenda.py i
```
###### Irá mostrar mostrar uma interface para listar/filtrar ou fazer/remover vários de uma vez. Não recebe parâmetros.

## Novidades
- [x] *[Projeto](https://github.com/Tiodonilo/ProjetoP1/tree/Projeto_1.0) funcional.*

- [x] *Filtragem dinâmica @Cont ou +Proj ou Cont/Proj.*

- [x] *Listagem dinâmica entre todos os extras e "ontem, hoje, amanhã".*

- [x] *[README.md](https://github.com/Tiodonilo/ProjetoP1/blob/Projeto_3.0/README.md) atualizado!*

- [x] *Help adicionado aos comandos, e várias adições e modificações!*

- [x] *Modularização da [datação](https://github.com/Tiodonilo/ProjetoP1/blob/Projeto_3.0/datacao.py) (ontem, hoje, amanhã) e do [programa](https://github.com/Tiodonilo/ProjetoP1/blob/Projeto_3.0/programa.py) principal.*

- [x] *Criação de uma [interface](https://github.com/Tiodonilo/ProjetoP1/blob/Projeto_3.0/interface.py) gráfica funcional, com ícone próprio.*

- [x] *Correção de bugs na interface, datação e afins.*

- [x] *Possibilidade de deletar/finalizar várias tarefas em uma só linha no Shell e adicionar mais de um projeto/pesquisa por comando!*

- [x] *Linhas de código mais enxutas com Docstrings!*

- [x] *Completamente compatível com linux.*

<p align="center">
<image src="./new.gif">
</p>

## Contribuidores
José Danilo, Centro de Informática, UFPE.
