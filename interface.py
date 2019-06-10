from tkinter import *
from functools import partial
from tkinter import ttk as t # (Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale and Scrollbar)
from agenda import listar, fazer, remover

def sair(janela):
    #registra(estoque)
    janela.destroy()

def volta(janela):
    janela.destroy()
    principal()

def logout(janela):
    #registra(estoque)
    janela.destroy()
    entrada()

def retirar(lista, janela):
        for i in lista:
                remover(i)
        volta(janela)

def finalizados():
        try:
                arquivo = open('done.txt', 'r')
                linhas = arquivo.readlines()
                arquivo.close()
                if linhas == []:
                        return ['Lista de atividades feitas.']
                return linhas
        except:
                return ['Lista de atividades feitas.']

def terminar(lista, janela):
        for i in lista:
                fazer(i)
        volta(janela)

def mostrar(elemento, lista):
        if elemento in lista:
                lista.remove(elemento)
        else:
                lista.append(elemento)
        print(lista)

def teste(lista, tarefas, param = 'n'):
        '''for widget in tarefas.winfo_children():
                if widget != '.!label':
                        widget.destroy()'''
        linhas = listar(param, 's')
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
        return linhas

def filtra(lista, tarefas, entrada):
        teste(lista, tarefas, entrada.get())

def principal():
        janela = Tk()
        window(janela)
        janela['bg'] = 'DarkOrchid3'
        estilo = t.Style()
        estilo.configure('TCheckbutton', background= "peach puff")
        estilo.configure('Y.TCheckbutton', background= "gold")
        estilo.configure('R.TCheckbutton', background= 'orangered')
        estilo.configure('TLabelFrame', background='DarkOrchid4')
        estilo.configure('C.TCheckbutton', background= 'DeepSkyBlue2')
        estilo.configure('G.TCheckbutton', background= 'SeaGreen2')

        lista = []
        topo = Frame(janela, bg='DarkOrchid4').pack(side=TOP, fill=X)
        baixo = Frame(janela, background='DarkOrchid2').pack(fill=X)
        label = t.Label(topo, text= 'TODO.TXT', font='arial 20', background='DarkOrchid4')
        tarefas = t.LabelFrame(baixo, text='Tarefas', height=200, width= 40)
        botoes = Frame(tarefas)
        enviar = t.Button(botoes, text='Finalizar Tarefas', command=partial(terminar, lista, janela))
        remove = t.Button(botoes, text='Remover Tarefas', command=partial(retirar, lista, janela))
        feitos = t.LabelFrame(baixo, text='Done', height=200, width=40)
        caixa = Listbox(feitos, bg= 'DarkOrchid2', fg='white', font='arial', width=30)
        filtro = Entry(baixo)
        b1 = t.Button(baixo, text='Filtrar', command= partial(filtra, lista, tarefas, filtro))

        label.pack(fill=X)
        tarefas.pack(side=LEFT)
        feitos.pack(side=LEFT)
        caixa.pack(side=LEFT)
        botoes.pack(side=BOTTOM)
        remove.pack(side=LEFT, padx=5)
        enviar.pack(side=RIGHT)
        filtro.pack()
        b1.pack()

        
        linhas2 = finalizados()
        linhas = teste(lista, tarefas, 'n')
        for i in linhas2:
                caixa.insert(END, i)
        janela.geometry('400x'+'10'*len(linhas)+'+550+300')
        janela.mainloop()

def acesso(usuario, senha, janela, label):
    global usuarios # Não precisa ser global
    if usuario.get() in usuarios:
            if usuarios[usuario.get()] == senha.get():
                    volta(janela)
            else:
                    label['text'] = 'Senha Inválida'
                    label['foreground'] = 'red'
    else:
            label['text'] = 'Usuário não cadastrado'
            label['foreground'] = 'red'

def entrada(): 
        janela = Tk()
        window(janela)
        janela.geometry('300x245+550+300')

        estilo = t.Style()
        estilo.configure("TLabel", width= 30, background='SpringGreen3', font= 'arial 12 bold', anchor='CENTER')
        estilo.configure('TButton', background='SpringGreen3')

        Label(janela, text='ACESSO', font='Georgia 20 bold', bg='SpringGreen3', fg='white').place(x=90, y=10)
        t.Label(janela, text='Login:', width=8, foreground='white', font='10').place(x=5, y=80) # bg='SpringGreen3',
        t.Label(janela, text='Senha:', width=8, foreground='white', font='10').place(x=5, y=120) # bg='SpringGreen3',

        label = t.Label(janela)
        login = t.Entry(janela, width= 30)
        senha = t.Entry(janela, width= 30, show='*')
        vazar = t.Button(janela, text='Sair', width=8, command= partial(sair, janela))
        entrar = t.Button(janela, text='Entrar', width=8, command= partial(acesso, login, senha, janela, label))

        login.place(x=75, y=80)
        senha.place(x=75, y=120)
        vazar.place(x=80, y=160)
        entrar.place(x=175, y=160)
        label.place(x= 17, y= 200)
        
        menu = Menu(janela)
        janela.config(menu=menu)
        menu.add_command(label='Sair', command=partial(sair, janela))

        janela.mainloop()

def window(janela):
    janela['bg'] = 'SpringGreen3'
    janela.title('Todo CheckList')
    janela.geometry('300x330+600+350')
    janela.iconbitmap('icone.ico')

    # Menu
    menu = Menu(janela)
    opcoes = Menu(menu)

    opcoes.add_command(label= 'Principal', command= partial(volta, janela))
    '''opcoes.add_separator()
    opcoes.add_command(label= 'Banco de Dados', command= partial(banco, janela))
    opcoes.add_command(label= 'Cadastrar', command= partial(cadastrar, janela))
    opcoes.add_command(label= 'Buscar', command=partial(search, janela))
    opcoes.add_command(label= 'Alterar', command=partial(alterar, janela))
    opcoes.add_command(label= 'Deletar', command=partial(deletar, janela))
    opcoes.add_separator()'''
    opcoes.add_command(label= 'Logout', command= partial(logout, janela))
    opcoes.add_command(label= 'Sair', command= partial(sair, janela))

    menu.add_cascade(label= 'Opções', menu= opcoes)
    janela.config(menu= menu)

usuarios = {'admin':'admin'}
entrada()
