import sys
from datacao import atual
from interface import entrada as inter
from programa import organizar, adicionar, listar

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'
AJUDA = 'h'
HOJE = 'hoje'
AGORA = 'agora'
AMANHA = 'amanha'
ONTEM = 'ontem'
INTERFACE = 'i'

def processarComandos(comandos) :
  
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
      remover(comandos[2])   
    except:
      print('ERROR: Digite um número! Válido!')
  elif comandos[1] == FAZER:
    try:
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
  Ordem:
    (Data) (hora) (prioridade) (tarefa) (contexto) (projeto) 
    
  Formato aceito:
    Data: DDMMAAAA (DiaMesAno)
    Hora: HHMM (HoraMinuto)
    Prioridade: (P) (A-Z)
    Tarefa: DESC
    Contexto: @CONTEXT
    Projeto: +PROJ''')
  elif comandos[1] == INTERFACE:
    inter()
  else :
    print("Comando inválido.")

try:
  processarComandos(sys.argv)
except:
  print('Nenhum comando passado!')