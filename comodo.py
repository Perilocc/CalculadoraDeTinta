class Comodo:
    __largura: float
    __profundidade: float
    __altura: float
    
    def __init__(self, largura, profundidade, altura ):
        self.largura = largura
        self.profundidade = profundidade
        self.altura = altura
    
    @property
    def largura(self):
        return self.__largura
    
    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def altura(self):
        return self.__altura
    
    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)
        except Exception:
            print('O valor da largura informado é inválido')
            exit()
        
    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print('O valor da profundidade informado é inválido')
            exit()
            
    @altura.setter
    def altura(self, altura):
        try:
            self.__altura = float(altura)
        except Exception:
            print('O valor da altura informado é inválido')
            exit()