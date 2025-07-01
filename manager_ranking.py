import json
import os
from jogador_ranking import JogadorRanking

class ManagerRanking:
    def __init__(self):
        self.__jogadores = []

    @property
    def jogadores(self):
        return self.__jogadores
    
    @jogadores.setter
    def jogadores(self, val: list):
        self.__jogadores = val
    
    def add_jogador(self, jogador: JogadorRanking):
        self.jogadores.append(jogador)
        
    def ordenar_e_limitar(self):
        self.jogadores.sort(key=lambda x: x.sequencia, reverse=True)
        self.jogadores = self.jogadores[:5]

    def salvar_ranking(self, nome_arquivo: str):
    # Verifica se a lista de jogadores não está vazia antes de salvar
        if not self.jogadores:
            print("Nenhum jogador no ranking para salvar!")
            return  # Se a lista estiver vazia, não salva o arquivo

        pasta_dados = os.path.join(os.path.dirname(__file__), 'dados')
        if not os.path.exists(pasta_dados):
            os.makedirs(pasta_dados)  # Cria a pasta 'dados' se não existir

        caminho = os.path.join(pasta_dados, nome_arquivo)
        print(f"Salvando no arquivo: {caminho}")

    # Salva os dados no arquivo JSON
        with open(caminho, "w") as f:
            json.dump([j.to_dict() for j in self.jogadores], f, indent=4)
            print(f"Ranking salvo no arquivo: {caminho}")


    def carrega_arquivo(self, nome_arquivo: str):
        pasta_dados = os.path.join(os.path.dirname(__file__), 'dados')
        caminho = os.path.join(pasta_dados, nome_arquivo)
        try:
            with open(caminho, "r") as f:
                try:
                    dados = json.load(f)
                    self.jogadores = [JogadorRanking.from_dict(j) for j in dados]
                    self.ordenar_e_limitar()
                except json.JSONDecodeError as e:
                    print(f"Erro ao decodificar o arquivo JSON: {e}")
                    self.jogadores = []
                except Exception as e:
                    print(f"Erro inesperado ao processar os dados JSON: {e}")
                    self.jogadores = []
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado. Criando novo ranking.")
            self.jogadores = []
        except Exception as e:
            print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")
            self.jogadores = []
