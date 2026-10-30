class CalculadoraDeVendas:
    def calcular_total(self, itens):
        return sum(item['preco'] * item['quantidade'] for item in itens)

    def aplicar_desconto(self, total, cliente):
        return total * 0.90 if cliente.get('tipo') == 'VIP' else total

class ProcessadorDePagamento:
    def processar(self, metodo_pagamento, total):
        if metodo_pagamento == 'CARTAO':
            print(f"Cobrando R$ {total} no cartão de crédito...")
        elif metodo_pagamento == 'BOLETO':
            print(f"Gerando boleto no valor de R$ {total}...")

class GeradorDeRelatorio:
    def salvar(self, cliente, total):
        relatorio = f"Relatório de Venda\nCliente: {cliente['nome']}\nTotal: R$ {total}\n"
        with open("relatorio_vendas.txt", "a") as f:
            f.write(relatorio)

class GerenciadorDeVendas:
    def __init__(self):
        self.calculadora = CalculadoraDeVendas()
        self.pagamento = ProcessadorDePagamento()
        self.relatorio = GeradorDeRelatorio()

    def processar_venda(self, itens, cliente, metodo_pagamento):
        total = self.calculadora.calcular_total(itens)
        total_com_desconto = self.calculadora.aplicar_desconto(total, cliente)
        
        self.pagamento.processar(metodo_pagamento, total_com_desconto)
        self.relatorio.salvar(cliente, total_com_desconto)
        
        print("Venda processada com sucesso.")
