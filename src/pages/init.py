import datetime
def app():
    dia_da_semana = datetime.datetime.now().strftime("%A")
    mes = datetime.datetime.now().month
    fase_dia= ''
    if 5 <= datetime.datetime.now().hour < 12:
        fase_dia = 'Morning'
    elif 12 <= datetime.datetime.now().hour < 18:
        fase_dia = 'Afternoon'
    elif 18 <= datetime.datetime.now().hour < 22:
        fase_dia = 'Evening'
    else:
        fase_dia = 'Night'
    frase = f"{dia_da_semana}, {mes} Good {fase_dia}, User"
    return frase