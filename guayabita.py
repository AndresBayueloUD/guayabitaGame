import random

def apuestaAleatoria(dineroMesa, montoJugador):
    if montoJugador<=dineroMesa:
        return (random.randrange(montoJugador/100)+1)*100
    else:
        return (random.randrange(dineroMesa/100)+1)*100

def guayabita(valorDadoAnt, dineroMesa, montoJugador1, montoJugador2, jugador, valorApostado): 
    if montoJugador1==0 or montoJugador2==0: 
        print("Jugador1->" + montoJugador1 + ", Jugador2->" + montoJugador2)
    elif dineroMesa == 0:
        return guayabita(0, dineroMesa+200, montoJugador1-100, montoJugador2-100, jugador, 0) 
    elif valorApostado > 0:
        if(random.randrange(6)+1) < valorDadoAnt: 
            if jugador==1: 
                return guayabita(0, dineroMesa+valorApostado, montoJugador1-valorApostado, montoJugador2, 2, 0) 
            else: 
                return guayabita(0, dineroMesa+valorApostado, montoJugador1, montoJugador2-valorApostado, 1, 0)
        else:
            if jugador==1: 
                return guayabita(0, dineroMesa-valorApostado, montoJugador1+valorApostado, montoJugador2, 2, 0) 
            else: 
                return guayabita(0, dineroMesa-valorApostado, montoJugador1, montoJugador2+valorApostado, 1, 0)
    elif valorDadoAnt == 0: 
        return guayabita(random.randrange(6)+1, dineroMesa, montoJugador1, montoJugador2, jugador, 0)
    elif valorDadoAnt == 1 or valorDadoAnt == 6: 
        if jugador==1: 
            return guayabita(0, dineroMesa+100, montoJugador1-100, montoJugador2, 2, 0) 
        else: 
            return guayabita(0, dineroMesa+100, montoJugador1, montoJugador2-100, 1, 0)
    elif valorDadoAnt == 2 or valorDadoAnt == 3 or valorDadoAnt == 4 or valorDadoAnt == 5:
        if jugador==1: 
            return guayabita(valorDadoAnt, dineroMesa, montoJugador1, montoJugador1, jugador, apuestaAleatoria(dineroMesa, montoJugador1))
        else: 
            return guayabita(valorDadoAnt, dineroMesa, montoJugador1, montoJugador2, jugador, apuestaAleatoria(dineroMesa, montoJugador2))

guayabita(0, 0, 1000, 1000, 1, 0)