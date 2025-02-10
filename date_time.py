from datetime import date, time, datetime, timedelta, timezone

# criar uma data específica
data_nascimento = date(1982, 12 , 25)
print("data de nascimento", data_nascimento)

# hora específica
hora_inicio = time(18, 30)
print("hora de início", hora_inicio)

# hora atual
hora_atual = datetime.now()
print("hora atual", hora_atual)

# hora específica
evento = datetime(2025, 2, 12, 18, 45, 30)
print("evento", evento)

# criando intervalo
intervalo = timedelta(days=5, hours=10)
print("intervalo", intervalo)
print(hora_atual+intervalo)
print(evento-hora_atual)

# criar uma data com fuso horario
timezone_brazil = timezone(timedelta(hours=-4))
date_utc = datetime.now(timezone_brazil)
print("date utc", date_utc)

# formatação das datas
print("hora atual formatada:", hora_atual.strftime("%d/%m/%Y %H:%M:%S"))
print("apenas a data:", hora_atual.strftime("%d/%b/%Y"))
print("apenas a hora:", hora_atual.strftime("%H:%M:%S"))

# convertendo uma string pra datetime
data_str = "06-02-2025 14:21" 
data_convertida = datetime.strptime(data_str, "%d-%m-%Y %H:%M")
print("Data convertida:", data_convertida)

print(intervalo+data_convertida)