import datetime
def app():
    dia_da_semana = datetime.datetime.now().strftime("%A")
    mes = datetime.datetime.now().month
    frase = f"{dia_da_semana}, {mes}/n Good Afternoon, User"
    return frase