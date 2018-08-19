import random

def f1(dineroMesa, minimaApuesta, dineroJugador1, dineroJugador2, jugador):
    print ("dinero mesa -> " + str(dineroMesa) + ", dinero jugador 1 -> " + str(dineroJugador1) + ", dinero jugador 2 -> " + str(dineroJugador2) + ", turno jugador -> " + str(jugador))
    if dineroJugador1 != 0 and dineroJugador2 != 0:
        if jugador==1:
            return f4(f2((random.randrange(6)+1), 0, dineroMesa, dineroJugador1, minimaApuesta, 0), dineroMesa, minimaApuesta, dineroJugador1, dineroJugador2, jugador)
        else:
            return f4(f2((random.randrange(6)+1), 0, dineroMesa, dineroJugador2, minimaApuesta, 0), dineroMesa, minimaApuesta, dineroJugador1, dineroJugador2, jugador)
    else:
        return "fin del juego"

def f2(valorDado, valorDadoAnt, dineroMesa, dineroJugador, minimaApuesta, valorApuesta):
    print ("valor dado -> " + str(valorDado))
    if valorApuesta > 0:
        print ("valor apuesta -> " + str(valorApuesta))
        if valorDado > valorDadoAnt:
            return valorApuesta
        else:
            return 0-valorApuesta
    elif valorDado == 1 or valorDado == 6:
        if dineroJugador >= minimaApuesta:
            return  0 - minimaApuesta
        else:
            return 0 - dineroJugador
    elif (valorDado == 2 or valorDado == 3 or valorDado == 4 or valorDado == 5) and dineroMesa >= minimaApuesta:
        return f2((random.randrange(6)+1), valorDado, dineroMesa, dineroJugador, minimaApuesta, f3(dineroMesa, dineroJugador))
    else:
        return 0

def f3(dineroMesa, montoJugador):
    if montoJugador<=dineroMesa:
        return (random.randrange(montoJugador/100)+1)*100
    else:
        return (random.randrange(dineroMesa/100)+1)*100

def f4(resultadoJuego, dineroMesa, minimaApuesta, dineroJugador1, dineroJugador2, jugador):
    if jugador==1:
        return f1(dineroMesa-resultadoJuego, minimaApuesta, dineroJugador1+resultadoJuego, dineroJugador2, 2)
    else:
        return f1(dineroMesa-resultadoJuego, minimaApuesta, dineroJugador1, dineroJugador2+resultadoJuego, 1)

print (f1(400, 100, 1000, 1000, 1))