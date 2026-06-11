import MainDb
import model.partidas
import tests.validations

#resetar e inicializar um novo um novo banco
MainDb.reset()
MainDb.initDb()

#Cores para o terminal
colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m"
}

#lista de times iniciais da fase 16 avos
timesIniciais = MainDb.teams

#Transforma uma lista de times em uma lista de duelos
def listaParaDuelos(equipes):
    duelos = []
    
    for i in range(0, len(equipes), 2):
        duelos.append([equipes[i], equipes[i + 1]])
    
    return duelos

#importa a classe partida em partidas.py
partida = model.partidas.partida

def resultadoDuelos(equipes, fase):
    vencedores = []
    duelos = listaParaDuelos(equipes)
    for duelo in duelos:
        resultado = partida.simularPartida(duelo[0], duelo[1], fase)
        print(f"vencedor de {duelo[0]}({resultado["gols_equipe1"]}) x {duelo[1]}({resultado["gols_equipe2"]}) = {resultado["vencedor"]}")
        
        vencedores.append(resultado["vencedor"])
    return vencedores

def iniciarCopaDoMundo():
    #validar dados antes de comecar
    tests.validations.validacoes(timesIniciais)
    
    #16 avos
    print(f"{colors['blue']}\n====FASE 16 AVOS====\n{colors['reset']}")
    resultado16Avos = resultadoDuelos(timesIniciais, "16 avos")

    #oitavas de final
    print(f"{colors['blue']}\n====FASE OITAVAS DE FINAL====\n{colors['reset']}")
    resultadoOitavas = resultadoDuelos(resultado16Avos, "oitavas de final")

    #quartas de final
    print(f"{colors['blue']}\n====FASE QUARTAS DE FINAL====\n{colors['reset']}")
    resultadoQuartas = resultadoDuelos(resultadoOitavas, "quartas de final")

    #semi-final
    print(f"{colors['blue']}\n====FASE SEMI-FINAL====\n{colors['reset']}")
    resultadoSemi = resultadoDuelos(resultadoQuartas, "semi-final")

    #final
    print(f"{colors['blue']}\n====FASE FINAL====\n{colors['reset']}")
    resultadoFinal = resultadoDuelos(resultadoSemi,"final")

    print(f"{colors['green']}VENCEDOR DA COPA DO MUNDO: {resultadoFinal[0]}{colors['reset']}")

def InfosGerais():
    print(f"{colors['purple']}\n====INFORMACOES E ESTATISTICAS====\n{colors['reset']}")
    
    print(f"{colors['purple']}Qual equipe marcou mais gols na competição?{colors['reset']}")
    maisGols = MainDb.ConsultarMaiorGoleador()
    for time, gols in maisGols:
        print(f"{time}: {gols} gols\n")
    
    print(f"{colors['purple']}Qual equipe sofreu menos gols na competição?{colors['reset']}")
    menosGols = MainDb.ConsultarEquipeMenosGols()
    for time, gols in menosGols:
        print(f"{time}: {gols} gols\n")
    
    print(f"{colors['purple']}Quantas partidas foram disputadas em cada fase?{colors['reset']}")
    
    for fase, quantidade in MainDb.ConsultarPartidasFases():
        print(f"{fase}: {quantidade} partidas")

iniciarCopaDoMundo()
InfosGerais()