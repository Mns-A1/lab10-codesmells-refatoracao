class Pais:
    def __init__(self, nome):
        self.nome = nome

class Estado:
    def __init__(self, nome, pais: Pais):
        self.nome = nome
        self.pais = pais
        
    def get_nome_pais(self):
        return self.pais.nome

class Endereco:
    def __init__(self, rua, estado: Estado):
        self.rua = rua
        self.estado = estado
        
    def get_pais_residencia(self):
        return self.estado.get_nome_pais()

class Cliente:
    def __init__(self, nome, endereco: Endereco):
        self.nome = nome
        self.endereco = endereco
        
    def eh_residente_internacional(self):
        return self.endereco.get_pais_residencia() != "Brasil"

class Pedido:
    def __init__(self, cliente: Cliente, valor):
        self.cliente = cliente
        self.valor = valor
        
    def requires_import_tax(self):
        return self.cliente.eh_residente_internacional()

def verificar_frete_internacional(pedido: Pedido):
    if pedido.requires_import_tax():
        print("Sujeito a taxa de importação.")
    else:
        print("Frete nacional padrão.")
