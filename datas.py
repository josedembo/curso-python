from datetime import date, time, datetime

def trabalhando_com_datetime():
    data_actual = datetime.now()
    print(data_actual.strftime("%d/%m/%Y %H:%M:%S"))
    print(data_actual.strftime("%c"))

def trabalhando_com_date():
    data_actual = date.today()
    print(data_actual)
    data_actual_str = data_actual.strftime("%d/%m/%Y")
    print(data_actual_str)

def trabalhando_com_time():
    hora = time(hour=15, minute=23, second=56)
    print(hora)


if __name__ == "__main__":
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()