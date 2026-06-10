import MainDb
import models.partidas

partida = models.partidas.partida
# MainDb.initDb()

#lista de times iniciais da fase 16 avos
timesIniciais = MainDb.teams

#Transforma uma lista de times em uma lista de duelos
def listaParaDuelos(equipes):
    duelos = []
    
    for i in range(0, len(equipes), 2):
        duelos.append([equipes[i], equipes[i + 1]])
    
    return duelos


def resultadoDuelos(equipes):
    vencedores = []
    duelos = listaParaDuelos(equipes)
    for duelo in duelos:
        resultado = partida.vencedor(duelo[0], duelo[1])
        print(f"vencedor de {duelo[0]}({resultado["gols_equipe1"]}) x {duelo[1]}({resultado["gols_equipe2"]}) = {resultado["vencedor"]}")
        
        vencedores.append(resultado["vencedor"])
    return vencedores


#16 avos
print("\n====FASE 16 AVOS====\n")
resultado16Avos = resultadoDuelos(timesIniciais)

#oitavas de final
print("\n====FASE OITAVAS DE FINAL====\n")
resultadoOitavas = resultadoDuelos(resultado16Avos)

#quartas de final
print("\n====FASE QUARTAS DE FINAL====\n")
resultadoQuartas = resultadoDuelos(resultadoOitavas)

#semi-final
print("\n====FASE SEMI-FINAL====\n")
resultadoSemi = resultadoDuelos(resultadoQuartas)

#final
print("\n====FASE FINAL====\n")
resultadoFinal = resultadoDuelos(resultadoSemi)

print(f"vencedor da Copa do mundo e :{resultadoFinal[0]}")