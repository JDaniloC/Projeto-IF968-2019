from functools import partial
from tkinter import ttk as t
from programa import listar, fazer, remover
import platform
from tkinter import *

def sair(janela):
    janela.destroy()

def volta(janela):
    janela.destroy()
    principal()

def logout(janela):
    janela.destroy()
    entrada()

def retirar(lista, janela):
        lista = [str(x) for x in sorted([int(y) for y in lista], reverse=True)]
        for i in range(len(lista)):
                remover(lista[i])
        volta(janela)

def finalizados():
        try:
                arquivo = open('done.txt', 'r')
                linhas = arquivo.readlines()
                arquivo.close()
                maior = len(max(linhas))
                if linhas == []:
                        return ['Lista de atividades feitas.']
                return linhas, maior
        except:
                return ['Lista de atividades feitas.'], 36

def terminar(lista, janela):
        lista = [str(x) for x in sorted([int(y) for y in lista], reverse=True)]
        for i in range(len(lista)):
                fazer(lista[i])
        volta(janela)

def mostrar(elemento, lista):
        if elemento in lista:
                lista.remove(elemento)
        else:
                lista.append(elemento)

def filtragem(lista, tarefas, param = 'n'):
        for widget in tarefas.winfo_children():
                widget.destroy()
        linhas = listar(param, 's')
        try: maior = len(max(linhas))
        except: maior = 1
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

def filtra(lista, tarefas, entrada): filtragem(lista, tarefas, entrada.get())

def principal():
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
        if ((tamanho+tamanho2)*10) > 505: tamanho = (tamanho+tamanho2)*10
        else: tamanho = 505
        if len(linhas) != 0 and len(linhas2) != 0:
                if len(linhas) > len(linhas2): tamanho2 = 100+(len(linhas)*23)
                else: tamanho2 = 100+(len(linhas2)*23)
        else: tamanho2 = 260

        janela.geometry(str(tamanho)+'x'+str(tamanho2)+'+550+300')
        janela.mainloop()

def acesso(usuario, senha, janela, label): # Foi retirado a possibilidade de se criar novos users.
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

def entrada(): 
        janela = Tk()
        window(janela)
        janela.geometry('300x245+550+300')

        estilo = t.Style()
        estilo.configure("TLabel", width= 30, background='SpringGreen3', font= 'arial 12 bold', anchor='CENTER')
        estilo.configure('TButton', background='SpringGreen3')

        Label(janela, text='ACESSO', font='Georgia 20 bold', bg='SpringGreen3', fg='white').place(x=90, y=10)
        t.Label(janela, text='Login:', width=8, foreground='white', font='10').place(x=5, y=80)
        t.Label(janela, text='Senha:', width=8, foreground='white', font='10').place(x=5, y=120)

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
