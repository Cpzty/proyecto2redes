import socket
from random import  randint
HOST = '127.0.0.1'
PORT = 65432

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
            elif(data.decode() == "play"):
                conn.sendall(b'yo')


