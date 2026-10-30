class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        
    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} CEP: {self.cep}"

class Contato:
    def __init__(self, ddd, telefone_numero):
        self.ddd = ddd
        self.telefone_numero = telefone_numero
        
    def __str__(self):
        return f"({self.ddd}) {self.telefone_numero}"

class Funcionario:
    def __init__(self, nome, cargo, salario, endereco: Endereco, contato: Contato):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco
        self.contato = contato

    def exibir_dados(self):
        print(f"Funcionário: {self.nome} ({self.cargo})")
        print(f"Contato: {self.contato}")
        print(f"Endereço: {self.endereco}")
