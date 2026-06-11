import logging
import sys

def validacoes(ListaTimes):
    #Verifica se existe a quantidade de paises correspondente para simular a Copa do Mundo
    if len(ListaTimes) != 32:
        logging.error(f"Quantidade inválida de países. Esperado: 32, encontrado: {len(ListaTimes)}.")
        sys.exit(1)

    for time in ListaTimes:
        vistos = set()
    
        #Verifica o padrao de escrita dos times
        if len(time) != 3:
            logging.error(f"Quantidade de caracteres para o país '{time}' invalida. Esperado: 3, encontrado: {len(time)}.")
            sys.exit(1)
        
        #Verifica se existem times repetidos    
        if time in vistos:
            logging.error(f"País duplicado encontrado: '{time}'")
            sys.exit(1)
            
        vistos.add(time)
