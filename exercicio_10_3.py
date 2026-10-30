class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Quarto:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo

class Reserva:
    def __init__(self, data_checkin, data_checkout, valor_diaria, possui_cafe_da_manha):
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.valor_diaria = valor_diaria
        self.possui_cafe_da_manha = possui_cafe_da_manha

    def calcular_total(self):
        total_dias = (self.data_checkout - self.data_checkin).days
        total = total_dias * self.valor_diaria
        if self.possui_cafe_da_manha:
            total += 50 * total_dias
        return total

def criar_reserva(hospede: Hospede, quarto: Quarto, reserva: Reserva):
    print(f"Reserva criada para {hospede.nome} (CPF: {hospede.cpf})")
    print(f"Quarto {quarto.numero} ({quarto.tipo})")
    print(f"De {reserva.data_checkin} até {reserva.data_checkout}")
    print(f"Total a pagar: R$ {reserva.calcular_total()}")
