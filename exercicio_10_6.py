class ProcessadorFinanceiro:
    def _validar_valor(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
    
    def _processar(self, valor, taxa, tipo_pagamento):
        self._validar_valor(valor)
        valor_com_taxa = valor + (valor * taxa)
        print(f"Processando {tipo_pagamento}: R$ {valor_com_taxa:.2f}")

    def processar_pagamento_credito(self, valor):
        self._processar(valor, 0.05, "crédito")

    def processar_pagamento_debito(self, valor):
        self._processar(valor, 0.02, "débito")
