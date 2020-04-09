from time import localtime, time
import calendar as c

def valores():
    '''
    -> Ira pegar o dia, mes, ano, hora, minuto de hoje e o dia de ontem e amanha.
    Ajusta qualquer valor 1-9 colocando um 0 na frente: 01 - 09.
    Ajusta caso ser dia 01, em pegar o ultimo dia do mes anterior (se 29-31).
    - Sem parâmetros

    Return [dia, mes, ano, hora, minuto, ontem, amanha];
    Onde [:5] sao de hoje, e [5:] sao o dia de ontem e amanha, todos em string.
    '''
    ano, mes, dia, hora, minuto = localtime(time())[:5]
    ontem, amanha = dia-1, dia+1

    mesPassado, esseMes = mes - 1, mes + 1
    if mesPassado == 0: mesPassado = 12
    if esseMes == 13: esseMes = 1

    mesPassado, esseMes = c.monthrange(ano, mesPassado)[1], c.monthrange(ano, esseMes)[1]
    if ontem == 0: ontem = mesPassado
    if amanha > esseMes: amanha = 1

    ano, mes, dia, hora, minuto, ontem, amanha = str(ano), str(mes), str(dia), str(hora), str(minuto), str(ontem), str(amanha)
    datas = [dia, mes, ano, hora, minuto, ontem, amanha]

    for i in range(7):
        if len(datas[i]) == 1:
            datas[i] = '0' + datas[i]
    
    return datas


def atual():
    '''
    -> Devolve o dia de hoje, ontem e amanha. E a hora/minuto do momento, em string.
    - Sem parametros

    Return (DiaDeHoje, HoraMinuto, DiaDeOntem, DiaDeAmanhã)
    '''
    datas = valores()
    today = datas[0] + datas[1] + datas[2]
    now = datas[3] + datas[4]
    yesterday = datas[5] + today[2:]
    tomorrow = datas[6] + today[2:]
    return today, now, yesterday, tomorrow
