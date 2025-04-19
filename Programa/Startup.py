import random

#A classe startup é o template de todas as startups, o que ha aqui estará em todas as startups com modificações.
class startup:
    def __init__(self, nome: str, slogan:str, ano_fundacao: int, pontuacao: int, carisma: int, qualidade: int, veracidade: int, ordem:int
                 ,investidores_irritados:int, bugs:int, penalidades:int, tracoes: int, pitches:int):
        self.nome = nome 
        self.slogan = slogan
        self.ano_fundacao = ano_fundacao
        self.pontuacao = pontuacao
        pontuacao = 70
        self.carisma = carisma
        self.qualidade = qualidade
        self.veracidade = veracidade
        self.ordem = ordem

        self.investidores_irritados = investidores_irritados
        self.bugs = bugs
        self.penalidades = penalidades
        self.tracoes = tracoes
        self.pitches = pitches

#Os getter e setters das variaveis serão necessarios para a função "set_rand_stats"
    @property
    def carisma(self):
        return self.__carisma
    
    @carisma.setter
    def carisma(self,carisma):
        self.__carisma = carisma
    
    @property
    def qualidade(self):
        return self.__qualidade
    
    @qualidade.setter
    def qualidade(self,qualidade):
        self.__qualidade = qualidade

    @property
    def veracidade(self):
        return self.__veracidade
    
    @veracidade.setter
    def veracidade(self,veracidade):
        self.__veracidade = veracidade

    #Esta função randomiza valores de carisma, qualidade e veracidade da startup. Estes valores serão utilizados na simulação das batalhas
    def set_rand_stats(self):
        self.carisma = random.randint(1, 10)
        self.qualidade = random.randint(1, 10)
        self.veracidade = random.randint(1, 10)
        self.ordem = random.randint(1, 5)

    #Esta função, como o nome ja indica, mostra todas as caracteristicas da startup.    
    def show_everything(self):
        print(f"Nome: {self.nome}")
        print(f"Slogan: {self.slogan}")
        print(f"Ano de fundação: {self.ano_fundacao}")
        print("-----Statisticas-----")
        print(f"Carisma: {self.carisma}")
        print(f"Qualidade: {self.qualidade}")
        print(f"Veracidade: {self.veracidade}")
        print(f"Ordem: {self.ordem}")
    
    def round_start(self):
        acao = random.randint(0,1)
        acao_str = ""

        bonus_perfect = 0
        irritados_rodada = 0
        bugs_rodada = 0
        tracoes_rodada = 0

        if acao == 0:
         #   print(f"A startup {self.nome} decidiu fazer um pitch")
            acao_str = "pitch"
            tracoes_rodada = random.randint(0, (10 - self.carisma))
            irritados_rodada = random.randint(0, (10 - self.veracidade))

            self.investidores_irritados += irritados_rodada
            self.tracoes += tracoes_rodada
            self.pitches += 1

            pontuacao_rodada = tracoes_rodada - irritados_rodada  

        elif acao == 1:
         #   print(f"A startup {self.nome} decidiu fazer uma build de seu produto")
            acao_str = "build"
            bugs_rodada = random.randint(0, (10 - self.qualidade))
            if bugs_rodada > 0:
                irritados_rodada = random.randint(0, (10 - self.veracidade) + 1)
            else:
                bonus_perfect = 5
            self.investidores_irritados += irritados_rodada
            self.bugs += bugs_rodada

            pontuacao_rodada = bonus_perfect - bugs_rodada - irritados_rodada
            

        infracoes_rodada = random.randint(0, (5 - self.ordem))
    
        if infracoes_rodada > 0:
            self.pontuacao -= infracoes_rodada * 2

        self.penalidades += infracoes_rodada
        self.pontuacao += pontuacao_rodada

        print("")
        print("Resumo da rodada: ")
        print(f"Startup: {self.nome}")
        print(f"Ação decidida: {acao_str}")
        print(f"Tração da rodada: {tracoes_rodada}")
        print(f"Investidores irritados da rodada: {irritados_rodada}")
        print(f"Bugs da rodada: {bugs_rodada}")
        print(f"Bonus: {bonus_perfect}")
        print(f"Infrações cometidas: {infracoes_rodada}")
        print(f"Pontos da rodada: {pontuacao_rodada}")
        print(f"Pontuação final: {self.pontuacao}")
        print("----------------------------------------------------------------")

