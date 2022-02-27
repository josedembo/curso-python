try:
    division = 7/1
    array_1 = [1, 2, 3, 4]
    accessing_array_1 = array_1[19]
except ZeroDivisionError as err:
    print("Um número não pode ser dividido por zero, Erro: {}".format(err))
except Exception as ex:
    print("Erro desconhecido, Erro: {}".format(ex))
else:
    print("executa qundo não ocorre excepção")
finally:
    print("sempre executa esse trecho de código")