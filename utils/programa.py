# Nomes para deixar arrumadinho.
TODO_FILE = 'todo.txt'
DONE_FILE = 'done.txt'

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"


def printCores(texto, cor) :
  '''
  -> Imprime texto com cores.
  Param texto = Texto a ser colorido.
  Param cor   = Cor do texto, fundo ou estilo.

  Cores:
    - RED     = Vermelho.
    - BLUE    = Azul.
    - CYAN    = Azul claro.
    - GREEN   = Verde.
    - BOLD    = Negrito.
    - REVERSE = Inverter cores.
    - YELLOW  = Amarelo.
  
  # Eh possivel juntar cor e estilo: YELLOW + BOLD
  Sem return.
  '''
  print(cor + texto + RESET)


def adicionar(descricao, extras, telegram = 'n'):
  '''
  -> Recebe a descricao e uma tupla/lista de extras e escreve no arquivo todo.txt
  Param descricao = Uma cadeia de strings relativos a tarefa em si.
  Param extras    = Uma lista/tupla referente a data, hora, prioridade e afins.

  A funcao considera que existem pelo menos 4 elementos nos extras:
  (data, hora, prioridade, outros)
  Dessa forma ela coloca a descricao apos o terceiro elemento.

  Return:
    Se houver descricao, e for possivel abrir o arquivo todo.txt, devolve True.
    Se não, devolve False.
  '''
  if descricao  == '' :
    if telegram == 'n':
      print('Nada adicionado: Sem Descrição!')
      return False
    else:
      return []
  else:
    novaAtividade = ''
    for i in range(len(extras)):
      if i == 3:
        novaAtividade += descricao + ' '
      if extras[i] != '':
        novaAtividade += extras[i] + ' '
  if telegram != 'n':
    return novaAtividade + '\n'
  try: 
    fp = open(TODO_FILE, 'a')
    fp.write(novaAtividade + "\n")
    fp.close()
    print('Adicionado com sucesso!')
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False
  return True


def prioridadeValida(pri):
  '''
  -> Recebe uma string e verifica tem exatamente tres caracteres;
  Se o primeiro e ‘(’, se o terceiro e ‘)’ e se o segundo e uma letra entre A e Z. 
  Funcionar tanto para letras minusculas quanto maiusculas. 
  
  Param pri = String, do formato (S), onde S = A-Z maiusculo ou minusculo.
  Return: Devolve True se as verificacoes passarem e False caso contrario.
  '''
  if len(pri) == 3 and pri[0] == '(' and pri[2] == ')' and ('A' <= pri[1] <= 'Z' or 'a' <= pri[1] <= 'z'):
    return True
  return False


def horaValida(horaMin) :
  '''
  -> Recebe uma string e verifica se ela tem exatamente quatro caracteres; 
  Se tao todos digitos, se os dois primeiros formam um numero entre 00 e 23;
  Se os dois ultimos formam um numero inteiro entre 00 e 59. 
  
  Param horaMin = String do formato HHMM, apenas numeros.
  Return: Se tudo isso for verdade, ela devolve True. Caso contrario, False. 
  '''
  if len(horaMin) == 4 and soDigitos(horaMin) and int(horaMin[:2]) < 24 and int(horaMin[2:]) < 60:
    return True
  else:
    return False


def dataValida(data) :
  '''
  -> Recebe uma string e verifica se tem exatamente oito caracteres;
  Se tao todos digitos e se os dois primeiros correspondem a um dia valido;
  Se o terceiro e o quarto correspondem a um mes valido e se os quatro ultimos correspondem a um ano valido. 
  Checa tambem se o dia e o mes fazem sentido juntos (se o dia poderia ocorrer naquele mes).
  Alem de verificar se o mes e um numero entre 1 e 12.
  Para fevereiro, considera que pode haver ate 29 dias, sem se preocupar se o ano e bissexto ou nao. 

  Param data = String do formato DDMMAAAA, apenas numeros.
  Return: Se todas as verificacoes passarem, devolve True. Caso contrario, False.
  '''
  if len(data) == 8 and soDigitos(data):
    dia, mes= int(data[:2]), int(data[2:4])
    if mes == 2:
      if 0 < dia < 30:
        return True
    else:
      if 0 < mes < 8 and ((mes % 2 != 0 and 0 < dia < 32) or (mes % 2 == 0 and 0 < dia < 31)):
        return True
      elif 7 < mes < 13 and ((mes % 2 != 0 and 0 < dia < 31) or (mes % 2 == 0 and 0 < dia < 32)):
        return True
  return False


def projetoValido(proj):
  '''
  -> Recebe uma string e verifica se tem pelo menos dois caracteres e se o primeiro eh ‘+’. 
  
  Param proj = String, do formato +String.
  Return: Devolve True se as verificacoes passarem e False caso contrario.
  '''
  if proj[0] == '+' and len(proj) > 2:
    return True
  return False


def contextoValido(cont):
  '''
  -> Recebe uma string e verifica se tem pelo menos dois caracteres e se o primeiro eh ‘@’. 
  
  Param cont = String, do formato @String.
  Return: Devolve True se as verificacoes passarem e False caso contrario.
  '''
  if cont[0] == '@' and len(cont) > 2:
    return True
  return False


def soDigitos(numero) :
  '''
  -> Recebe uma string e verifica se cada caracter sao apenas numeros.

  Param numero = String.
  Return: Devolve True se as verificacoes passarem e False caso contrario.
  '''
  if type(numero) != str :
    return False
  for x in numero :
    if x < '0' or x > '9' :
      return False
  return True


def organizar(linhas):
  '''
  -> Devolve uma lista de tuplas com as informações das atividades organizadas.
  Param linhas = Uma lista de strings representando atividades.

  Atualizacao 2.0: Transforma as prioridades em maiusculas.
  Atualizacao 3.0: Aceita mais de um projeto/descricao.
  Return: Devolve uma tupla de strings do formato (descricao,(data, hora, prioridade, contexto, projeto...))
  '''
  itens = []
  for l in linhas:
    data, hora, pri, desc = '', '', '', '',
    l = l.strip()
    tokens = l.split() 
    if dataValida(tokens[0]):
      data = tokens.pop(0)
    if horaValida(tokens[0]):
      hora = tokens.pop(0)
    if prioridadeValida(tokens[0]):
      pri = (tokens.pop(0)).upper()
    projcont = ()
    while tokens != [] and (projetoValido(tokens[-1]) or contextoValido(tokens[-1])):
      if tokens != [] and projetoValido(tokens[-1]):
        projcont += tokens.pop(-1),
      if tokens != [] and contextoValido(tokens[-1]):
        projcont += tokens.pop(-1),
    while len(projcont) < 2: projcont += '',
    desc = ' '.join(tokens)
    extras = (data, hora, pri) + projcont
    itens.append((desc, extras))
  return itens


def filtragem(linhas, ordem, conteudo):
  '''
  -> Prepara uma tarefa para a apresentacao no listar.
  1   - Verifica se a prioridade eh A - D. Se True = 1.1, caso contrario 1.2.
    1.1 - Transforma a prioridade em maiusculo e joga para frente da tarefa.
    1.2 - Joga "N" para frente da tarefa.
  2   - Joga o indice original na frente da tarefa.
  3   - Verifica se ha extras e formata da forma correta.
    3.1 - Transforma a data DD/MM/AAAA.
    3.2 - Transforma a hora HH:MM.
    3.3 - Coloca a descricao antes do contexto.
    3.4 - Adiciona espacos depois de cada extra/descricao.

  Param linhas   = A tarefa em questão
  Param ordem    = Uma lista que despoe do indice das linhas na ordem original
  Param conteudo = Lista com todas as linhas
  Return: Uma cadeia de string de formato:
  "(prioridade)(Indice) (data)(hora)(prioridade)(descricao)(contexto ou pesquisa)..."
  '''
  textinho = ''
  if linhas[1][2] != '':
    if 'A' <= linhas[1][2][1] <= 'D':
      textinho += linhas[1][2][1]
    elif 'a' <= linhas[1][2][1] <= 'd': # Ou coloca um "or" no if de cima.
      textinho += (linhas[1][2][1]).upper()
    else:
      textinho += 'N'
  else:
    textinho += 'N'
  textinho += str(ordem[conteudo.index(linhas)]) + ' '
  for extras in range(len(linhas[1])):
    if extras == 0 and linhas[1][0] != '':
      textinho += linhas[1][0][:2] + '/' + linhas[1][0][2:4] + '/' + linhas[1][0][4:] + ' '
    elif extras == 1 and linhas[1][1] != '':
      textinho += linhas[1][1][:2] + ':' + linhas[1][1][2:] + ' '
    elif extras == 3:
      textinho += linhas[0] + ' '
      if linhas[1][extras] != '':
        textinho += linhas[1][extras] + ' '
    else: 
      if linhas[1][extras] != '': textinho += linhas[1][extras] + ' '
  return textinho
  

def listar(filtro = 'n', inter= 'n', telegram= 'n'):
  '''
  -> Imprime na tela as tarefas no arquivo todo.txt
  1 - Tenta executar todo o programa, caso contrario emite um erro.
  2 - Faz um dicionario com o indice original de cada tarefa.
  3 - Ordena por data/hora, depois por prioridade.
  4 - Rearranja a ordem de acordo com a nova ordenacao e coloca numa lista.
  5 - Adiciona cada tarefa numa lista de acordo com o principio de filtragem.
  6 - Imprime cada tarefa de acordo com suas cores e o total de tarefas exibidas. #NOVO

  Param filtro = Caso for passado, entao filtra as tarefas para apenas as que tem tal string.
  Param inter = Caso passado devolve uma lista das tarefas.
  return: Se inter diferente de "n", devolve uma lista de cada tarefa de forma organizada.
  '''
  try:
    if telegram == 'n':
      fp = open(TODO_FILE, 'r')
      linhas = fp.readlines()
      fp.close()
    else:
      linhas = telegram
    conteudo = organizar(linhas)

    tarefas = {}
    for i in range(len(conteudo)):
      tarefas[i+1] = conteudo[i]
    
    conteudo = ordenarPorPrioridade(ordenarPorDataHora(conteudo))
    ordem = []
    for itens in conteudo:
      for key, values in tarefas.items():
        if values == itens:
          ordem.append(key)
          break
    
    textos = []
    if filtro == 'n':
      for linhas in conteudo:
        textos.append(filtragem(linhas, ordem, conteudo))
    else:
      filtros = ['@'+filtro, '+'+filtro, '('+filtro.upper()+')', filtro, filtro.upper()]
      for linhas in conteudo:
        if len([x for x in linhas[1] if x in filtros]) > 0:
          textos.append(filtragem(linhas, ordem, conteudo))
    
    if inter != 'n' or telegram != 'n':
      lista = []
      for tarefinhas in textos:
        lista.append(tarefinhas)
      return lista

    for tarefinhas in textos:
      if tarefinhas[0] == 'A':
        printCores(tarefinhas[1:], YELLOW + BOLD)
      elif tarefinhas[0] == 'B':
        printCores(tarefinhas[1:], RED)
      elif tarefinhas[0] == 'C':
        printCores(tarefinhas[1:], BLUE)
      elif tarefinhas[0] == 'D':
        printCores(tarefinhas[1:], GREEN)
      else:
        print(tarefinhas[1:])
    print(f'--\nTODO: Mostrando {len(textos)} de {len(conteudo)}')

  except IOError as err:
    print("Não foi possível ler o arquivo " + TODO_FILE)
    print(err)


def datainverso(data):
  '''
  -> Inverte a data para poder comparar qual a maior.
  Param data = String, do formato DDMMAAA.

  return: String da data invertida.
  '''
  data = int(data[4:] + data[2:4] + data[:2])
  return data


def ordenarPorDataHora(itens):
  '''
  -> Ordena os itens de acordo com a data/hora, os mais recentes primeiro.
  1 - Verifica aqueles sem data e adiciona numa lista.
  2 - Ordena aqueles com data, onde os mais recentes vem primeiro.
    2.1 - Se forem iguais, ele ordena de acordo com a hora.
  3 - Verifica aqueles sem hora na lista dos sem data e adiciona numa lista.
  4 - Ordena os sem data de acordo com a hora.
  5 - Cria uma nova lista ordenada do formato: (data)(semData)(semHora)

  Param itens = Lista de tarefas.
  return: Lista ordenada de tarefas.
  '''
  semData= []
  i = 0
  while i != len(itens):
    if itens[i][1][0] == '':
      semData.append(itens.pop(i))
      i -= 1
    i += 1
  for vezes in range(len(itens)-1):
    for x in range(len(itens)-1):
      if datainverso(itens[x][1][0]) > datainverso(itens[x+1][1][0]):
        aux = itens[x]
        itens[x] = itens[x+1]
        itens[x+1] = aux
      elif datainverso(itens[x][1][0]) == datainverso(itens[x+1][1][0]):
        if itens[x][1][1] != '' and itens[x+1][1][1] != '':
          if int(itens[x][1][1]) > int(itens[x+1][1][1]):
            aux = itens[x]
            itens[x] = itens[x+1]
            itens[x+1] = aux
  semHora = []
  i = 0
  while i != len(semData):
    if semData[i][1][1] == '':
      semHora.append(semData.pop(i))
      i -= 1
    i += 1
  for vezes in range(len(semData)-1):
    for x in range(len(semData)-1):
      if int(semData[x][1][1]) > int(semData[x+1][1][1]):
        aux = semData[x]
        semData[x] = semData[x+1]
        semData[x+1] = aux
  itens = itens + semData + semHora
  return itens


def ordenarPorPrioridade(itens):
  '''
  -> Ordena uma lista de tarefas pela prioridade.
  1 - Verifica aqueles sem prioridade e adiciona numa lista.
  2 - Ordena de acordo com a maior prioridade A > Z.
  3 - Devolve uma nova lista do formato: (comPrioriadadeOrdenados)(semPrioridade)

  Param itens = Uma lista de tarefas.
  return: Lista ordenada de tarefas de acordo com a prioridade.
  '''
  vazio = []
  i = 0
  while i != len(itens):
    if itens[i][1][2] == '':
      vazio.append(itens.pop(i))
      i -= 1
    i += 1
  for vezes in range(len(itens)-1):
    for x in range(len(itens)-1):
      if (itens[x][1][2]).upper() > (itens[x+1][1][2]).upper():
        aux = itens[x]
        itens[x] = itens[x+1]
        itens[x+1] = aux
  return itens + vazio


def fazer(num):
  '''
  -> Retira a tarefa desejada do todo.txt e adiciona no done.txt
  1 - Pega a tarefa com a funcao remover.
  2 - Se houver tarefa, adiciona a tarefa no done.txt. 

  Param num = String, indice da tarefa.
  Nao devolve nada.
  '''
  variavel = remover(num, 's')
  if variavel != '!':
    try: 
      arquivo = open(DONE_FILE, 'a')
      arquivo.write(variavel)
      arquivo.close()
      print('Operação realizada com sucesso!')
    except IOError as err:
      print("Não foi possível escrever para o arquivo " + DONE_FILE)
      print(err)


def remover(atividade, faz = 'n'):
  '''
  -> Remove uma tarefa do todo.txt.
  1 - Verifica se a atividade selecionada eh valida.
  2 - Cria um novo arquivo sem a tarefa selecionada.

  Param atividade = String, indice da atividade desejada.
  Param faz = Se diferente de "n", devolve a atividade selecionada depois de remove-la.
  return: Se faz != "n", devolve a tarefa desejada, depois de remove-la.
  '''
  fp = open(TODO_FILE, 'r')
  linhas = fp.readlines()
  fp.close()
  if 0 > int(atividade) or int(atividade) > len(linhas):
    print('Não consta na lista!')
    if faz != 'n':
      return '!'
  else:
    fp = open(TODO_FILE, 'w')
    for i in range(len(linhas)):
      if i != int(atividade)-1:
        fp.write(linhas[i])
      else:
        linha = linhas[i]
    fp.close()
    if faz != 'n':
      return linha
    printCores('Operação realizada com sucesso!', REVERSE)


def priorizar(num, prioridade, telegram = 'n'):
  '''
  -> Adiciona/modifica a prioridade de uma tarefa.
  1 - Adiciona () na prioridade nova se nao tiver. #NEW!
  2 - Verifica se eh uma prioridade valida.
  3 - Verifica se o indice consta no todo.txt.
  4 - Pega a tarefa e remonta com a nova prioridade.
  5 - Reescreve o todo.txt com a nova atividade no local correto.

  Param num = String, indice da prioridade.
  Param prioridade = String, prioridade no formato a-Z ou (A)-(z).
  Nao devolve nada.
  '''
  if telegram == 'n':
    fp = open(TODO_FILE, 'r')
    linhas = fp.readlines()
    fp.close()
  else:
    linhas = telegram
  if prioridade[0] != '(':
    prioridade = '('+prioridade.upper()+')'
  if prioridadeValida(prioridade):
    if 0 > int(num) > len(linhas):
      print('Não consta na lista!')
      if telegram != 'n':
        return 'Não consta na lista!'
    else:
      for i in range(len(linhas)):
        if i == int(num)-1:
          tarefa = organizar([linhas[i]])[0]
      desc = tarefa[0]
      extras = list(tarefa[1])
      extras[2] = prioridade.upper()
      extras.insert(3, desc) # Ou extras = extras[:3] + [desc] + extras[3:]
      extras = ' '.join([x for x in extras if x != ''])
      if telegram != 'n':
        linhas[int(num)-1] = extras
        return linhas
      novo = open(TODO_FILE, 'w')
      for i in range(len(linhas)):
        if i == int(num)-1:
          novo.write(extras+ '\n')
        else:  
          novo.write(linhas[i])
      novo.close()
      printCores('Operação realizada com Sucesso!', REVERSE)
  else:
    print('Insira uma prioridade válida: A,B,C,D... ou (A),(B),(C)...')
