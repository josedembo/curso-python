
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    def subtr(self):
        return self.valor_a - self.valor_b

    def mult(self):
        return self.valor_a * self.valor_b

    def div(self):
        return self.valor_a / self.valor_b

calc_1 = Calculadora(10, 2)

print("soma entre {} e {} = {}".format(calc_1.valor_a, calc_1.valor_b, calc_1.soma()) )
print("subtração entre {} e {} = {}".format(calc_1.valor_a, calc_1.valor_b, calc_1.subtr()) )

class Calculadora_2:
    def __init__(self):
        pass
