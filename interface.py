from functools import partial
from tkinter import ttk as t
from programa import listar, fazer, remover
import platform
from tkinter import *

def sair(janela):
        '''
        -> Fecha a janela referenciada.
        Param janela = Instancia de Tk que quer fechar.
        Sem return.
        '''
        janela.destroy()

def volta(janela):
        '''
        -> Fecha a janela referenciada e abre a funcao principal.
        Param janela = Instancia de Tk.
        Sem return.
        '''
        janela.destroy()
        principal()

def logout(janela):
        '''
        -> Fecha a janela referenciada e abre a funcao entrada.
        Param janela = Instancia de Tk.
        Sem return.
        '''
        janela.destroy()
        entrada()

def retirar(lista, janela):
        '''
        -> Remove as tarefas atraves do indice dado numa lista.
        1 - Transforma os indices em Inteiros e ordenada a lista. # NEW
        2 - Inverte a lista e tranforma em String novamente. # NEW
        3 - Usa a funcao remover para cada item.
        Vai para a funcao volta.

        Param lista  = Lista de strings com os indices que quer remover.
        Param janela = Instancia de Tk.
        Sem return.
        '''
        lista = [str(x) for x in sorted([int(y) for y in lista], reverse=True)]
        for i in range(len(lista)):
                remover(lista[i])
        volta(janela)

def finalizados():
        '''
        -> Mostra as tarefas no done.txt.
        1 - Abre o arquivo done.txt e ve se existe algum item.
                1.1 - Se nao, ele devolve uma lista de String e 36.
                1.2 - Se sim, devolve a lista de tarefas e o len do maior elemento.
        
        Sem parametros.
        return: lista de strings e len do maior string, se tiver algum elemento no todo.txt
        (['Lista de atividades feitas'], 36), se nao.
        '''
        try:
                arquivo = open('done.txt', 'r')
                linhas = arquivo.readlines()
                arquivo.close()
                maior = len(max(linhas))
                return linhas, maior
        except:
                return ['Lista de atividades feitas.'], 36

def terminar(lista, janela):
        '''
        -> Remove as tarefas atraves do indice numa lista e adicionar no done.txt.
        1 - Transforma os indices em Inteiros e ordenada a lista. # NEW
        2 - Inverte a lista e tranforma em String novamente. # NEW
        3 - Usa a funcao fazer para cada item.
        Vai para a funcao volta.

        Param lista  = Lista de strings com os indices que quer mover.
        Param janela = Instancia de Tk.
        Sem return.
        '''
        lista = [str(x) for x in sorted([int(y) for y in lista], reverse=True)]
        for i in range(len(lista)):
                fazer(lista[i])
        volta(janela)

def mostrar(elemento, lista):
        '''
        -> Adiciona ou remove um indice numa lista referenciada pelo checkbutton.
        Se o item ja esta na lista ele remove (quando o checkbutton eh desselecionado)
        Se nao, ele adiciona o indice na lista.
        
        Param elemento = String, indice da tarefa.
        Param lista = A lista que vai ser adicionada/removida.
        Sem return.
        '''
        if elemento in lista:
                lista.remove(elemento)
        else:
                lista.append(elemento)

def filtragem(lista, tarefas, param = 'n'):
        '''
        -> Filtra os elementos do todo.txt.
        1 - Reseta todos os elementos no Labelframe.
        2 - Recebe as tarefas atraves da funcao listar.
        3 - Tenta ver o len da maior tarefa.
                3.1 - Se tiver uma variavel recebe o tamanho.
                3.2 - Se nao, entao a variavel recebe 1.
        4 - Verifica se existe algum elemento na lista de tarefas.
                4.1 - Se sim, ele adiciona um Checkbutton para cada um, onde:
                        4.1.1 - O texto fica amarelo se tiver prioridade A.
                        4.1.2 - O texto fica laranja se tiver prioridade B.
                        4.1.3 - O texto fica cyan se tiver prioridade C.
                        4.1.4 - O texto fica verde se tiver prioridade D.
                        4.1.5 - O texto fica cor de pele se nao tiver prioridade.
                4.2 - Se nao, adicionar um Checkbutton padrao.

        Param lista   = Uma lista que os Checkbuttons vao adicionar os indices.
        Param tarefas = O Labelframe que as tarefas vao ser jogadas.
        Param param   = Um parametro para a funcao listar.
        return: Se tiver tarefas, (lista de tarefas, len do maior elemento)
        Se nao, ([], 1)
        '''
        for widget in tarefas.winfo_children():
                widget.destroy()
        linhas = listar(param, 's')
        try: maior = len(max(linhas))
        except: maior = 1
        if type(linhas) == list:
                for i in linhas:
                        if i[0] == 'A':
                                t.Checkbutton(tarefas, text= i[3:], style= 'Y.TCheckbutton', command= partial(mostrar, i[1:3], lista)).pack(fill=X)
                        elif i[0] == 'B':
                                t.Checkbutton(tarefas, text= i[3:], style= 'R.TCheckbutton', command= partial(mostrar, i[1:3], lista)).pack(fill=X)
                        elif i[0] == 'C':
                                t.Checkbutton(tarefas, text= i[3:], style= 'C.TCheckbutton', command= partial(mostrar, i[1:3], lista)).pack(fill=X)
                        elif i[0] == 'D':
                                t.Checkbutton(tarefas, text= i[3:], style= 'G.TCheckbutton', command= partial(mostrar, i[1:3], lista)).pack(fill=X)
                        else:
                                t.Checkbutton(tarefas, text= i[3:], style= 'TCheckbutton', command= partial(mostrar, i[1:3], lista)).pack(fill=X)
                return linhas, maior
        else:
                t.Checkbutton(tarefas, text= 'Nenhuma tarefa', style= 'Y.TCheckbutton').pack(fill=X)
                return [], 1

def filtra(lista, tarefas, entrada): filtragem(lista, tarefas, entrada.get())

def principal():
        '''
        -> Funcao com a tela principal.
        Sem param.
        Sem return.
        '''
        janela = Tk()
        window(janela)
        janela['bg'] = 'PaleGreen3'
        estilo = t.Style()
        estilo.configure('TCheckbutton', background= "peach puff")
        estilo.configure('Y.TCheckbutton', background= "gold")
        estilo.configure('R.TCheckbutton', background= 'orangered')
        estilo.configure('TLabelFrame', background='SpringGreen4')
        estilo.configure('C.TCheckbutton', background= 'DeepSkyBlue2')
        estilo.configure('G.TCheckbutton', background= 'SeaGreen2')

        lista = []
        topo = Frame(janela, bg='SpringGreen4').pack(side=TOP, fill=X)
        baixo = Frame(janela, background='PaleGreen2').pack(fill=X)
        label = t.Label(topo, text= 'TODO.TXT', font='arial 20', background='SpringGreen4')
        tarefas = t.LabelFrame(baixo, text='Tarefas', height=200, width= 40)
        botoes = Frame(topo)
        enviar = t.Button(botoes, text='Finalizar Tarefas', command=partial(terminar, lista, janela))
        remove = t.Button(botoes, text='Remover Tarefas', command=partial(retirar, lista, janela))
        filtro = Entry(botoes, width=37)
        pesquisar = t.Button(botoes, text='Filtrar', command= partial(filtra, lista, tarefas, filtro))
        feitos = t.LabelFrame(baixo, text='Done', width=40)
        scroll = Scrollbar(feitos)
        caixa = Listbox(feitos, bg= 'PaleGreen2', fg='black', font='verdana 8 bold', width=30, yscrollcommand=scroll.set)
        scroll.config(command= caixa.yview)

        label.pack(fill= X)
        botoes.pack(side= TOP)
        remove.pack(side= LEFT, padx= 5)
        filtro.pack(side= LEFT)
        pesquisar.pack(side= LEFT)
        enviar.pack(side= LEFT)
        tarefas.pack(side= LEFT)
        feitos.pack(side= LEFT, padx= 1)
        scroll.pack(side= RIGHT, fill= Y)
        caixa.pack(side= LEFT, fill= X)
        
        linhas2, tamanho = finalizados()
        linhas, tamanho2 = filtragem(lista, tarefas, 'n')
        for i in linhas2:
                caixa.insert(END, i)
        caixa['height'] = len(linhas)+11
        caixa['width'] = tamanho
        if ((tamanho+tamanho2)*10) > 505: 
                tamanho = (tamanho+tamanho2)*10
        else: 
                if platform.system() == "Windows": tamanho = 505
                else: tamanho = 505 + 135
        if len(linhas) != 0 and len(linhas2) != 0:
                if len(linhas) > len(linhas2): tamanho2 = 100+(len(linhas)*23)
                else: tamanho2 = 100+(len(linhas2)*23)
        else: tamanho2 = 260
        if platform.system() == 'Windows': janela.geometry(str(tamanho)+'x'+str(tamanho2)+'+550+300')
        else: janela.geometry(str(tamanho)+'x'+str(tamanho2)+'+'+str(750-int(tamanho/2))+'+'+str(300-int(tamanho2/2)))
        janela.mainloop()

def acesso(usuario, senha, janela, label): # Foi retirado a possibilidade de se criar novos users.
        '''
        -> Verifica se o usuario e senha estao corretos.
        Se sim, entra na funcao volta.
        Se nao, mostra um texto no Label.

        Param usuario = Um Entry.
        Param senha   = Um Entry.
        param janela  = Instancia de Tk.
        Param label   = Label para mostrar onde errou.
        Sem return.
        '''
        usuarios = {'admin':'admin'}
        if usuario.get() in usuarios:
                if usuarios[usuario.get()] == senha.get():
                        volta(janela)
                else:
                        label['text'] = 'Senha Inválida'
                        label['foreground'] = 'red'
        else:
                label['text'] = 'Usuário não cadastrado'
                label['foreground'] = 'red'

def apaga(login, event): login.delete(0, END)
def apaga2(senha, event): 
        senha.delete(0, END)
        senha['show'] = '*'

def entrada(): 
        '''
        -> Tela de Login.
        Com tamanho ajustado para Linux! # NEW

        Sem Param.
        Sem return.
        '''
        janela = Tk()
        window(janela)
        janela.geometry('300x245+750+400')

        estilo = t.Style()
        estilo.configure("TLabel", width= 30, background='SpringGreen3', font= 'arial 12 bold', anchor='CENTER')
        estilo.configure('TButton', background='SpringGreen3')

        Label(janela, text='ACESSO', font='Georgia 20 bold', bg='SpringGreen3', fg='white').place(x=90, y=10)
        t.Label(janela, text='Login:', width=8, foreground='white', font='10').place(x=5, y=80)
        t.Label(janela, text='Senha:', width=8, foreground='white', font='10').place(x=5, y=120)

        label = t.Label(janela)
        login2 = Frame(janela, bd= 0, highlightthickness=0)
        senha2 = Frame(janela, bd= 0, highlightthickness=0)
        if platform.system() == 'Windows': 
                login = Entry(login2, width= 22, relief=FLAT, background='SpringGreen3', fg='white', font='impact 11')
                login.insert(0, 'Login')
                login.bind('<Button-1>', partial(apaga, login))
                senha = Entry(senha2, width= 22, relief=FLAT, background='SpringGreen3', fg='white', font='impact 11')
                senha.insert(0, 'Senha')
                senha.bind('<Button-1>', partial(apaga2, senha))
        else: 
                login = Entry(login2, width= 22, relief=FLAT, background='SpringGreen3', fg='white', font='FreeMono 11', highlightthickness=0)
                login.insert(0, 'Login')
                login.bind('<Button-1>', partial(apaga, login))
                senha = Entry(senha2, width= 22, show='*', relief=FLAT, background='SpringGreen3', fg='white', font='impact 11', highlightthickness=0)
                senha.insert(0, 'Senha')
                senha.bind('<Button-1>', partial(apaga2, senha))
        vazar = t.Button(janela, text='Sair', width=8, command= partial(sair, janela))
        entrar = t.Button(janela, text='Entrar', width=8, command= partial(acesso, login, senha, janela, label))

        login2.place(x=75, y=80)
        login.pack(pady=(0,1))
        senha2.place(x=75, y=120)
        senha.pack(pady=(0,1))
        vazar.place(x=80, y=160)
        entrar.place(x=175, y=160)
        label.place(x= 17, y= 200)
        
        menu = Menu(janela)
        janela.config(menu=menu)
        menu.add_command(label='Sair', command=partial(sair, janela))

        janela.mainloop()

def window(janela):
        '''
        -> Atalho para configurar a janela de forma rapida.
        Adiciona as configuracoes padroes das janelas que chamarem a funcao.
        Com icone atualizado para o Linux! # NEW

        Param janela = Instancia de Tk.
        Sem return
        '''
        janela['bg'] = 'SpringGreen3'
        janela.title('Todo CheckList')
        janela.geometry('300x330+600+350')
        if platform.system() == 'Windows':
                janela.iconbitmap("icone.ico")
        else:
                janela.iconbitmap('@icone.xbm')
        
        menu = Menu(janela)
        opcoes = Menu(menu)

        opcoes.add_command(label= 'Principal', command= partial(volta, janela))
        opcoes.add_separator()
        opcoes.add_command(label= 'Logout', command= partial(logout, janela))
        opcoes.add_command(label= 'Sair', command= partial(sair, janela))

        menu.add_cascade(label= 'Opções', menu= opcoes)
        janela.config(menu= menu)
