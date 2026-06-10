import random

class partida:
    def __init__(self, fase):
        self.fase = fase
        
    def vencedor(equipe1, equipe2):
        gols_equipe1 = random.randint(0, 10)
        gols_equipe2 = random.randint(0, 10)
        
        resultado = {
            "vencedor": "",
            "gols_equipe1": gols_equipe1,
            "gols_equipe2": gols_equipe2
        }
        
        if gols_equipe1 > gols_equipe2:
            resultado["vencedor"] = equipe1
            return resultado
        
        elif gols_equipe1 < gols_equipe2:
            resultado["vencedor"] = equipe2
            return resultado
        
        #em caso de empate
        elif gols_equipe1 == gols_equipe2:
            resultado["vencedor"] = random.choice([equipe1, equipe2])
            return resultado