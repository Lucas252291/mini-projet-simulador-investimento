class investimento():
    def __init__(self, percentual_input, aporte_inicial, recorrente):
        self.percentual = percentual_input / 100.0  # Armazena como decimal (ex: 100 -> 1.0)
        self.aporte_inicial = float(aporte_inicial)
        self.recorrente = recorrente
        self.total_investido = float(aporte_inicial)  # Inicialmente, o total investido é o depósito inicial
        self.valor_atual = float(aporte_inicial)      # Valor atual, começa com o depósito inicial