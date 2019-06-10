from tkinter import *
from functools import partial
from tkinter import ttk as t # (Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale and Scrollbar)
from agenda import listar

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

def mostrar(elemento, lista):
        if elemento in lista:
                lista.remove(elemento)
        else:
                lista.append(elemento)
        print(lista)

def principal():
        janela = Tk()
        window(janela)
        estilo = t.Style()
        estilo.configure('TCheckbutton', background='SpringGreen2')
        janelinha1 = Frame(janela, bg='SpringGreen3', height=10)
        janelinha1.pack(fill= X)
        janelinha2 = Frame(janela, bg='SpringGreen2', height=30)
        janelinha2.pack(fill= X)

        label = Label(janelinha1, text= 'LISTA', font='arial 20', bg='SpringGreen3')
        label.pack()

        lista = []
        linhas = listar('n', 's')
        for i in linhas:
                t.Checkbutton(janelinha2, text= i[2:], command= partial(mostrar, i[:2], lista)).pack(fill=X)
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
    janela.geometry('300x330+550+300')
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
