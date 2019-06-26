import sys
from datacao import atual
from interface import entrada as inter
from programa import organizar, adicionar, listar, fazer, remover, priorizar
from imail import enviar

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'
AJUDA = 'h'
INTERFACE = 'i'
ENVIAR = 'e'
HOJE = 'hoje'
AGORA = 'agora'
AMANHA = 'amanha'
ONTEM = 'ontem'

def processarComandos(comandos, telegram = 'n') :
  '''
  -> Direciona a outras funções a partir dos seguintes comandos:
  ADICIONAR = a (adiciona uma nova task).
  REMOVER   = r (remove alguma task pelo index).
  FAZER     = f (remove a task do todo.txt e coloca no done.txt).
  PRIORIZAR = p (insere/modifica alguma prioridade pelo index).
  LISTAR    = l (mostra as tasks do todo.txt).
  AJUDA     = h (Mostra como proceder em cada função).
  INTERFACE = i (Acelera processos).
  ENVIAR    = e (Envia o todo.txt por email).
  
  -> Também aceita datação dinamica, atraves dos seguintes comandos:
  HOJE   = hoje   (O dia de hoje DDMMAAAA).
  AGORA  = agora  (A hora e minuto do momento HHMM).
  AMANHA = amanha (O dia de amanha DDMMAAAA).
  ONTEM  = ontem  (O dia de ontem DDMMAAAA).
  
  Sem return.
  '''
  today, now, yesterday, tomorrow = atual() # Pegar o dia e hora de hoje, ontem e amanhã.
  strdatas, datas = [AGORA, HOJE, ONTEM, AMANHA], [now, today, yesterday, tomorrow]
  if len(comandos) > 2:
    if (comandos[2]).lower() in strdatas[1:]:
      comandos[2] = datas[strdatas.index(comandos[2])]
      if len(comandos) > 3 and (comandos[3]).lower() == AGORA: comandos[3] = now
    elif (comandos[2]).lower() == AGORA:
      comandos[2] = now
  
  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'adicionar'
    lista, lista2 = [], []
    if '~~' in comandos: # Vê se tá tentando adicionar vários.
      comandos.append('~~')
      for i in range(len(comandos)):
        if comandos[i] == '~~' and len(lista2) != 0:
          lista.append(' '.join(lista2))
          lista2 = []
          if len(comandos[i:]) > 2:
            if (comandos[i+1]).lower() in strdatas[1:]:
              comandos[i+1] = datas[strdatas.index(comandos[i+1])]
              if len(comandos[i:]) > 3 and (comandos[i+2]).lower() == 'agora': comandos[i+2] = datas[0]
            elif (comandos[i+1]).lower() == 'agora': comandos[i+1] = datas[0]
        elif comandos[i] == '~~': pass
        else: lista2.append(comandos[i])
      itemParaAdicionar = organizar(lista)
    else:
      itemParaAdicionar = organizar([' '.join(comandos)]) #[0]
    # itemParaAdicionar = (descricao, (prioridade, data, hora, contexto, projeto))
    if telegram == 'n':
      for i in itemParaAdicionar:
        adicionar(i[0], i[1])
    else:
      for i in itemParaAdicionar:
        return adicionar(i[0], i[1], 's')
  elif comandos[1] == LISTAR:
    print('Tarefas:\n')
    if telegram == 'n':
      try:
        listar(comandos[2])
      except:
        listar()
    else:
      try:
        return listar(comandos[2], 'n', telegram)
      except:
        return listar('n', 'n', telegram)
  elif comandos[1] == REMOVER:
    try:
      if len(comandos[2:]) > 1:
        lista = comandos[2:]
        lista = [str(x) for x in sorted([int(y) for y in lista], reverse=True)]
        for elemento in lista:
          remover(elemento)
      else:
        remover(comandos[2])   
    except:
      print('ERROR: Digite um número! Válido!')
  elif comandos[1] == FAZER:
    try:
      if len(comandos[2:]) > 1:
        lista = comandos[2:]
        lista = [str(x) for x in sorted([int(y) for y in lista], reverse=True)]
        for elemento in lista:
          print(elemento)
          fazer(elemento)
      else:
        fazer(comandos[2])
    except:
      print('ERROR: Digite um número válido!')
  elif comandos[1] == PRIORIZAR:
    if telegram == 'n':
      try:
        priorizar(comandos[2], comandos[3])
      except:
        print('N° Atividade, A-Z!')
    else:
      try:
        return priorizar(comandos[2], comandos[3], telegram)
      except:
        return 'N° Atividade, A-Z!'
  elif comandos[1] == AJUDA:
    print('''
  Ordem de inserção:
  a (Data) (hora) (prioridade) (tarefa) (contexto) (projeto) 
    
  Formato aceito:
    Data:       DDMMAAAA (DiaMesAno)
    Hora:       HHMM     (HoraMinuto)
    Prioridade: (P)      (A-Z)
    Tarefa:     DESC
    Contexto:   @CONTEXT
    Projeto:    +PROJ
  
  Funções:
  Adicionar: a (Data) (hora) (prioridade) (tarefa) (contexto) (projeto)
    - Todos são opcionais menos a tarefa.
    - Pode adicionar mais de um separando as tarefas com um "~~"
    - A data pode ser substituida por: hoje, amanha, ontem
    - A hora pode ser substituida por: agora
    - Prioridade pode ser:             (A) (a) - (a) (A)
    - Contexto:                        Pode ser colocado mais de um.
    - Projeto:                         Pode ser colocado mais de um.
  Remover: r (indice)...
    - Pode remover mais do que um, colocando varios indices separados por espaço.
  Listar: l (data, hora, prioridade, contexto, projeto)
    - Se sozinho, ira aparecer todos do todo.txt.
    - Se nao colocar o sinal do contexto/projeto, ira aparecer ambos.
  Fazer: f (indice)...
    - Pode fazer mais do que um, colocando varios indices separados por espaço.
  Priorizar: p (indice) (prioridade)
    - Formatos aceitos: (A) (a) a
  Interface: i
    - Não recebe argumentos.
  Email: e
    - Envia o todo.txt por email!
    - Não recebe argumentos.
    - Pede o email, se não tiver @, então adiciona @gmail.com
    
  Favor rodar no Prompt/Shell.''')
  elif comandos[1] == INTERFACE:
    inter()
  elif comandos[1] == ENVIAR:
    if telegram == 'n':
      enviar(input('Digite o seu email: '), listar('n', 's'))
    else:
      return enviar(telegram[0], listar('n', 'n', telegram[1]), 's')
  else :
    print(comandos)
    print("Comando inválido.")

try:
  processarComandos(sys.argv)
except:
  print('Nenhum comando passado!')