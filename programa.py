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

# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  print(cor + texto + RESET)

def adicionar(descricao, extras):
  if descricao  == '' :
    print('Nada adicionado: Sem Descrição!')
    return False
  else:
    novaAtividade = ''
    for i in range(len(extras)):
      if i == 3:
        novaAtividade += descricao + ' '
      if extras[i] != '':
        novaAtividade += extras[i] + ' '
  try: 
    fp = open(TODO_FILE, 'a')
    fp.write(novaAtividade + "\n")
    fp.close()
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False
  return True

def prioridadeValida(pri):
  if len(pri) == 3 and pri[0] == '(' and pri[2] == ')' and ('A' <= pri[1] <= 'Z' or 'a' <= pri[1] <= 'z'):
    return True
  return False

def horaValida(horaMin) :
  if len(horaMin) == 4 and soDigitos(horaMin) and int(horaMin[:2]) < 24 and int(horaMin[2:]) < 60:
    return True
  else:
    return False

def dataValida(data) :
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
  if proj[0] == '+' and len(proj) > 2:
    return True
  return False

def contextoValido(cont):
  if cont[0] == '@' and len(cont) > 2:
    return True
  return False

def soDigitos(numero) :
  if type(numero) != str :
    return False
  for x in numero :
    if x < '0' or x > '9' :
      return False
  return True

def organizar(linhas):
  itens = []
  for l in linhas:
    data, hora, pri, desc, contexto, projeto = '', '', '', '', '', ''
    l = l.strip()
    tokens = l.split() 
    if dataValida(tokens[0]):
      data = tokens.pop(0)
    if horaValida(tokens[0]):
      hora = tokens.pop(0)
    if prioridadeValida(tokens[0]):
      pri = (tokens.pop(0)).upper()
    if tokens != [] and projetoValido(tokens[-1]):
      projeto = tokens.pop(-1)
    if tokens != [] and contextoValido(tokens[-1]):
      contexto = tokens.pop(-1)
    desc = ' '.join(tokens)
    itens.append((desc, (data, hora, pri, contexto, projeto)))
  return itens 

def filtragem(linhas, ordem, conteudo):
  textinho = ''
  if linhas[1][2] != '':
    if 'A' <= linhas[1][2][1] <= 'D':
      textinho += linhas[1][2][1]
    elif 'a' <= linhas[1][2][1] <= 'd':
      textinho += (linhas[1][2][1]).upper()
    else:
      textinho += 'N'
  else:
    textinho += 'N'
  textinho += str(ordem[conteudo.index(linhas)]) + ' '
  for extras in range(5):
    if extras == 0 and linhas[1][0] != '':
      textinho += linhas[1][0][:2] + '/' + linhas[1][0][2:4] + '/' + linhas[1][0][4:] + ' '
    elif extras == 1 and linhas[1][1] != '':
      textinho += linhas[1][1][:2] + ':' + linhas[1][1][2:] + ' '
    elif extras == 2 and linhas[1][2] != '':
      textinho += linhas[1][extras] + ' '
    elif extras == 3:
      textinho += linhas[0] + ' '
      if linhas[1][extras] != '':
        textinho += linhas[1][extras] + ' '
    elif extras == 4:
      textinho += linhas[1][extras]
      return textinho
  
def listar(filtro = 'n', inter= 'n'):
  try: 
    fp = open(TODO_FILE, 'r')
    linhas = fp.readlines()
    conteudo = organizar(linhas)
    fp.close()

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
      filtros = ['@'+filtro, '+'+filtro, '('+filtro.upper()+')', filtro]
      for linhas in conteudo:
        if filtros[0] in linhas[1] or filtros[1] in linhas[1] or filtros[2] in linhas[1] or filtros[3] in linhas[1]:
          textos.append(filtragem(linhas, ordem, conteudo))
    
    if inter != 'n':
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

  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)

def datainverso(data):
  data = int(data[4:] + data[2:4] + data[:2])
  return data

def ordenarPorDataHora(itens):
  semData= []
  i = 0
  while i != len(itens):
    if itens[i][1][0] == '':
      semData.append(itens.pop(i))
      i -= 1
    i += 1
  for vezes in range(len(itens)-1):
    for x in range(len(itens)-1):
      if datainverso(itens[x][1][0]) < datainverso(itens[x+1][1][0]):
        aux = itens[x]
        itens[x] = itens[x+1]
        itens[x+1] = aux
      elif datainverso(itens[x][1][0]) == datainverso(itens[x+1][1][0]):
        if itens[x][1][1] != '' and itens[x+1][1][1] != '':
          if int(itens[x][1][1]) < int(itens[x+1][1][1]):
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
      if int(semData[x][1][1]) < int(semData[x+1][1][1]):
        aux = semData[x]
        semData[x] = semData[x+1]
        semData[x+1] = aux
  itens = itens + semData + semHora
  return itens
   
def ordenarPorPrioridade(itens):
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

def priorizar(num, prioridade):
  fp = open(TODO_FILE, 'r')
  linhas = fp.readlines()
  fp.close()
  if prioridade[0] != '(':
    prioridade = '('+prioridade.upper()+')'
  if prioridadeValida(prioridade):
    if 0 > int(num) or int(num) > len(linhas):
      print('Não consta na lista!')
    else:
      for i in range(len(linhas)):
        if i == int(num)-1:
          tarefa = organizar([linhas[i]])[0]
      desc = tarefa[0]
      extras = list(tarefa[1])
      extras[2] = prioridade.upper()
      extras.insert(3, desc) # Ou extras = extras[:3] + [desc] + extras[3:]
      extras = ' '.join([x for x in extras if x != ''])
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