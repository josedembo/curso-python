class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        nota = int(input("Informe um valor de 0 a 10: "))
        if nota > 10:
            raise InputError("O valor não pode ser maior do que zero")
        if nota < 0:
            raise InputError("O valor não poder ser menor do que zero")
        print(nota)
        break
    except ValueError:
        print("valor ínvalido, deve ser digitado apenas números")
    except InputError as err:
        print("Error: {}".format(err))
