# coding: utf-8
import telepot
from agenda import processarComandos

bot = telepot.Bot("737574969:AAHgaEmqn2jkzSW5shewX-U1jS8R8-VpK1s")

def listou(comando):
    '''
    -> Mostra as tarefas da lista.
    Param comando = comandos no estilo ProcessarComandos.
    return: string, string.
    '''
    if len(lista) == 0:
        return 'Nenhuma tarefa.', 'TODO: Mostrando 0 de 0.\n'
    tasks = processarComandos(comando, lista)
    texto = ''
    for i in tasks:
        texto += i[1:] + '\n'
    total = '--\nTODO: Mostrando '+ str(len(tasks)) +' de '+ str(len(lista))
    return texto, total

def retira(comando):
    '''
    -> Remove a tarefa da lista.
    Param comando = Indice.
    return: String, dependendo do resultado.
    '''
    try:
        if 0 < int(comando) < len(lista)+1:
            lista.pop(int(comando)-1)
            return 'Tarefa retirada com sucesso!'
        else:
            return 'Não está na lista!'
    except:
        return 'Comando inválido'

def receiver(msg):
    '''
    -> Pega cada mensagem do usuario e processa os comandos.
    Param msg = Mensagem do usuario.
    Sem return.
    '''
    global lista, tutorial
    pergunta = msg['text']
    if pergunta != None:
        tmsg, tcht, pessoa = telepot.glance(msg)
        if pergunta == '/start':
            nome = msg['from']['first_name'] + ' ' + msg['from']['last_name']
            bot.sendMessage(pessoa, ('Olá '+nome+' bem-vindo ao todo.txt!'))
            bot.sendMessage(pessoa, 'Para acessar comandos, digite "/"')
        else:
            if pergunta[0] == '!':
                comando = ['agenda.py'] + pergunta[1:].split()
                variavel = processarComandos(comando)
            else:
                comando = ['agenda.py'] + pergunta.split()
                if comando[1] == 'a':
                    if len(comando) > 2:
                        variavel = processarComandos(comando, 's')
                        if type(variavel) == str:
                            lista.append(variavel)
                            print(lista)
                            bot.sendMessage(pessoa, 'Adicionado com Sucesso!')
                        else:
                            bot.sendMessage(pessoa, 'Algo de errado não está certo...')
                    else:
                        bot.sendMessage(pessoa, 'Precisa de pelo menos uma tarefa né...')
                elif comando[1] == 'l':
                    texto, total = listou(comando)
                    bot.sendMessage(pessoa, 'Tarefas:')
                    bot.sendMessage(pessoa, texto)
                    bot.sendMessage(pessoa, total)
                elif comando[1] == 'r':
                    if len(comando) > 2:
                        if len(comando[2:]) > 1:
                            comandos = [str(x) for x in sorted([int(y) for y in comando[2:]], reverse=True)]
                            for i in comandos:
                                texto = retira(i)
                                bot.sendMessage(pessoa, texto)
                        else:
                            texto = retira(comando[2])
                            bot.sendMessage(pessoa, texto)
                    else:
                        bot.sendMessage(pessoa, 'Digite o indice!')
                elif comando[1] == 'p':
                    variavel = processarComandos(comando, lista)
                    if type(variavel) == list:
                        lista = variavel
                        bot.sendMessage(pessoa, 'Priorizado com sucesso!')
                    else:
                        bot.sendMessage(pessoa, variavel)
                elif comando[1] == 'e':
                    if len(comando) > 2:
                        mensagem = processarComandos(comando, (comando, lista))
                        bot.sendMessage(pessoa, mensagem)
                    else:
                        bot.sendMessage(pessoa, 'Precisa de um e-mail!')
                else:
                    bot.sendMessage(pessoa, tutorial)

tutorial = ''' COMO USAR
# Se você está controlando o todo.txt numa máquina local, e armazenando em um arquivo, então digite "!" antes de qualquer função.
O bot funciona da mesma forma que o script, porém sem guardar em um arquivo (com excessão do caso acima).

Adicionar = a (Data) (hora) (prioridade) (tarefa) (contexto) (projeto), apenas a descrição é obrigatória.
    Formato aceito:
        Data:       DDMMAAAA (DiaMesAno)
        Hora:       HHMM     (HoraMinuto)
        Prioridade: (P)      (A-Z)
        Tarefa:     DESC
        Contexto:   @CONTEXT
        Projeto:    +PROJ
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
Fazer: f (indice)... # SÓ ESTA DISPONIVEL PARA EM MAQUINA LOCAL, NÃO TEM NECESSIDADE ONLINE!
    - Pode fazer mais do que um, colocando varios indices separados por espaço.
Priorizar: p (indice) (prioridade)
    - Formatos aceitos: (A) (a) a
Email: e (email)
    - Se não tiver @, então adiciona @gmail.com
'''

lista = []
bot.message_loop(receiver)
while True:
    pass
