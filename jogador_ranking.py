class JogadorRanking:
    def __init__(self, nome: str, pontuacao: int, sequencia: int):
        self.__nome = nome
        self.__pontuacao = pontuacao
        self.__sequencia = sequencia
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @property
    def sequencia(self):
        return self.__sequencia
    
    @nome.setter
    def nome(self, val: str):
        self.__nome = val

    @pontuacao.setter
    def pontuacao(self, val: int):
        self.__pontuacao = val
    
    @sequencia.setter
    def sequencia(self, val: int):
        self.__sequencia = val
    
    def to_dict(self):
        return {"nome": self.nome, "pontuacao": self.pontuacao, "sequencia": self.sequencia}
        
    @staticmethod
    def from_dict(data):
        return JogadorRanking(data["nome"], data["pontuacao"], data["sequencia"])
    
    def __repr__(self):
        return f"{self.nome}: {self.pontuacao} com {self.sequencia} vitorias seguidas"
