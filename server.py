import socket
from random import  randint
HOST = '127.0.0.1'
PORT = 65432

rooms = []
puntaje_p1 = 0
puntaje_p2 = 0
puntaje_p3 = 0
puntaje_p4 = 0

def repartir_cartas():
    palo = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    baraja = palo + palo + palo + palo
    p1_cards = []
    p2_cards = []
    p3_cards = []
    p4_cards = []
    for i in range(13):
        p1_cards.append(baraja.pop(randint(0, len(baraja) - 1)))
        p2_cards.append(baraja.pop(randint(0, len(baraja) - 1)))
        p3_cards.append(baraja.pop(randint(0, len(baraja) - 1)))
        p4_cards.append(baraja.pop(randint(0, len(baraja) - 1)))

    return p1_cards, p2_cards, p3_cards, p4_cards


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            #conn.sendall(data)
            #elif("create" in data.decode()):
            elif (data.decode() == "PIN"):
                pin = str(randint(1,9)) + str(randint(1,9)) + str(randint(1,9))
                conn.send(pin.encode())
            elif ("A" in data.decode()):
                ataque = data.decode().split()
                carta = ataque[1]
                atacado = ataque[2]
                #restarle puntaje al otro jugador
                #conn.send()
            elif("S" in data.decode()):
                #averiguar que jugador lo envia para sumarse puntaje
                puntaje_p1 = puntaje_p1 + int(data.decode())
            elif("R" in data.decode()):
                robo = data.decode().split()
                carta = robo[1]
                robado = robo[2]
                #enviar al jugador correspondiente determinar exito o fracaso y reenviar al jugador inicial