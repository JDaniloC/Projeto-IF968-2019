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

def processarComandos(comandos) :
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
  if len(comandos) > 2:
    if (comandos[2]).lower() == HOJE:
      comandos[2] = today
    elif (comandos[2]).lower() == AGORA:
      comandos[2] = now
    elif (comandos[2]).lower() == AMANHA:
      comandos[2] = tomorrow
    elif (comandos[2]).lower() == ONTEM:
      comandos[2] = yesterday
    if len(comandos) > 3 and (comandos[3]).lower() == AGORA:
      comandos[3] = now
  
  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'adicionar'
    itemParaAdicionar = organizar([' '.join(comandos)])[0]
    # itemParaAdicionar = (descricao, (prioridade, data, hora, contexto, projeto))
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1]) # novos itens não têm prioridade
  elif comandos[1] == LISTAR:
    print('Tarefas:\n')
    try:
      listar(comandos[2])
    except:
      listar()
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
    try:
      priorizar(comandos[2], comandos[3])
    except:
      print('N° Atividade, A-Z!')
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
  Email: e #NEW
    - Envia o todo.txt por email!
    - Não recebe argumentos.
    - Pede o email, se não tiver @, então adiciona @gmail.com
    
  Favor rodar no Prompt/Shell.''')
  elif comandos[1] == INTERFACE:
    inter()
  elif comandos[1] == ENVIAR:
    enviar(input('Digite o seu email: '), listar('n', 's'))
  else :
    print(comandos)
    print("Comando inválido.")

try:
  processarComandos(sys.argv)
except:
  print('Nenhum comando passado!')