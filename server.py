import socket
from random import  randint
from _thread import *
import threading

some_lock = threading.Lock()
rooms = []
puntaje_p1 = 0
puntaje_p2 = 0
puntaje_p3 = 0
puntaje_p4 = 0
adresses = []


def threaded_server(con):
    while True:
        data = con.recv(1024)
        if not data:
            break
        # conn.sendall(data)
        # elif("create" in data.decode()):
        elif (data.decode() == "PIN"):
            pin = str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9))
            con.send(pin.encode())
        elif ("A" in data.decode()):
            ataque = data.decode().split()
            carta = ataque[1]
            atacado = ataque[2]
            # restarle puntaje al otro jugador
            # conn.send()
        elif ("S" in data.decode()):
            # averiguar que jugador lo envia para sumarse puntaje
            puntaje_p1 = puntaje_p1 + int(data.decode())
        elif ("R" in data.decode()):
            robo = data.decode().split()
            carta = robo[1]
            robado = robo[2]
            # enviar al jugador correspondiente determinar exito o fracaso y reenviar al jugador inicial
        elif(data.decode() == "lista"):
            for i in range(len(adresses)):
                adress = adresses[i]
                adress_response = "address: " + str(adress)
                con.send(adress_response.encode())


def Main():
    HOST = '127.0.0.1'
    PORT = 65432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("socket binded to port", PORT)
    s.listen(5)
    while True:
        # establish connection with client
        con, addr = s.accept()

        # lock acquired by client
        some_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
        if addr[1] not in adresses:
            adresses.append(addr[1])

        # Start a new thread and return its identifier
        t1 = threading.Thread(target=threaded_server(con))
        t1.start()
    s.close()


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


if __name__ == '__main__':
    Main()