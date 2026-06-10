import random
import MainDb

class partida:        
    def simularPartida(equipe1, equipe2, fase):
        #simula o resultado dos jogos randomicamente
        gols_equipe1 = random.randint(0, 10)
        gols_equipe2 = random.randint(0, 10)
        
        #inserir partida atual no banco
        partida_id = MainDb.inserirPartidas(fase, equipe1, equipe2)
        
        #Atualiza gols pro e contra das equipes atuais
        MainDb.atualizarGols(gols_equipe1, gols_equipe2, equipe1)
        MainDb.atualizarGols(gols_equipe2, gols_equipe1, equipe2)
        
        resultado = {
            "vencedor": "",
            "perdedor": "",
            "gols_equipe1": gols_equipe1,
            "gols_equipe2": gols_equipe2
        }
        
        if gols_equipe1 > gols_equipe2:
            resultado["vencedor"] = equipe1
            resultado["perdedor"] = equipe2
        
        elif gols_equipe1 < gols_equipe2:
            resultado["vencedor"] = equipe2
            resultado["perdedor"] = equipe1
        
        #em caso de empate
        elif gols_equipe1 == gols_equipe2:
            vencedor = random.choice([equipe1, equipe2])
            resultado["vencedor"] = vencedor
            resultado["perdedor"] = equipe2 if vencedor == equipe1 else equipe1
        
        MainDb.inserirResultados(partida_id, resultado["vencedor"], resultado["perdedor"])
        return resultado