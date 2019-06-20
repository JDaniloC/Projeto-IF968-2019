import smtplib

def textoformatado(string):
    '''
    -> Recebe uma cadeia de strings e devolve-a sem acentos.
    Param string = Cadeia de strings.
    return: NovaCadeiaDeStrings+"\n"
    '''
    string = (string[1:]).strip()
    textinho = ''
    invalidos = ['ã', 'á', 'â', 'à', 'é', 'ê', 'í', 'ó', 'ô', 'ú', 'ç', 'ñ']
    aceitos = ['a', 'a', 'a', 'a', 'eh', 'e', 'i', 'o', 'o', 'u', 'c', 'n']
    for i in string:
        if 127 > ord(i) > 31:
            textinho += i
        else:
            for a in range(len(invalidos)):
                if i == invalidos[a]:
                    textinho += aceitos[a]
    return textinho + '\n'

def enviar(email, tasks):
    '''
    -> Recebe um email e tarefas e envia para o email desejado.
    Param email = email destino, se nao tiver @, ele adiciona @gmail.com.
    Param tasks = Tarefas numa lista.
    Sem return.
    '''
    if '@' not in email:
        email += '@gmail.com'
    if type(tasks) == list:
        tasks = ''.join([textoformatado(x) for x in tasks])
        usuario = 'todotxtcin@gmail.com'  
        senha = 'Python123'

        de = usuario  
        para = ['todotxtcin@gmail.com', email]  
        assunto = 'TODO.TXT Tasks'  
        tarefas = tasks

        texto = """\  
        De: %s  
        Para: %s  
        Assunto: %s

%s
        """ % (de, ", ".join(para), assunto, tarefas)
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(usuario, senha)
            server.sendmail(de, para, texto)
            server.close()

            print ('Email Enviado!')
        except:  
            print ('Alguma coisa deu errado...')
