class Bola:
    def __init__(self, cor: str, circunferencia: float, material: str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor: str):
        self.cor = nova_cor

    def mostraCor(self):
        print(f"a Cor da bola é: {self.cor}")

# ---------------------------------------------------------------------------------

class Quadrado:
    def __init__(self, tamanho: float):
        self.tamanho = tamanho

    def mudarTamanho(self, novo_tamanho: float):
        self.tamanho = novo_tamanho

    def retornarTamanho(self):
        return self.tamanho

    def calcularArea(self):
        return self.tamanho ** 2

# ---------------------------------------------------------------------------------

class Retangulo:
    def __init__(self, comprimento, largura: float):
        self.comprimento = comprimento
        self.largura = largura

    def mudarValor(self, novo_comprimento, nova_largura: float):
        self.comprimento = novo_comprimento
        self.largura = nova_largura

    def retornarValor(self):
        return self.comprimento, self.largura

    def calcularArea(self):
        return self.comprimento * self.largura

    def calcularPerimetro(self):
        return (self.comprimento + self.largura) * 2

# ---------------------------------------------------------------------------------
