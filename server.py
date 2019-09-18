import socket
from random import  randint
from _thread import *
import threading

some_lock = threading.Lock()
rooms = {"room1":
             {"pin": 0,
         "p1" : '',
         "p2" : '',
         "p3" : '',
         "p4" : '',
         "count" : 0},
         "room2":
            {"pin": 0,
         "p1" : '',
         "p2" : '',
         "p3" : '',
         "p4" : '',
         "count" : 0},
         }

adresses = []

players = ["p1", "p2", "p3", "p4"]
players2 = ["p1", "p2", "p3", "p4"]

clients = {}

p1_cards = []
p2_cards = []
p3_cards = []
p4_cards = []

def threaded_server(con, addr):
    puntaje_p1 = 0
    puntaje_p2 = 0
    puntaje_p3 = 0
    puntaje_p4 = 0
    #global p1_cards, p2_cards, p3_cards, p4_cards
    while True:
        data = con.recv(1024)
        if not data:
            break
        # conn.sendall(data)
        # elif("create" in data.decode()):

        #juego
        elif(data.decode() == "sala"):
            if(rooms["room1"]["count"] == 4):
                ready_to_play(con, addr)
            else:
                con.send("no".encode())

        elif (data.decode() == "PIN"):
            pin = str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9))
            if rooms["room1"]["pin"] == 0:
                con.send(pin.encode())
                rooms["room1"]["pin"] = pin

            elif(rooms["room2"]["pin"] == 0):
                con.send(pin.encode())
                rooms["room2"]["pin"] = pin

            else:
                con.send(b'error creating pin')
        elif ("A" in data.decode()):
            ataque = data.decode().split()
            carta = ataque[1]
            atacado = ataque[2]
            quien_ataca = ataque[3]
            # restarle puntaje al otro jugador
            if(addr == rooms["room1"][atacado]):
                carta_atacado = "A " + carta
                con.send(carta_atacado.encode())
                if(quien_ataca == "p1"):
                    if(addr == rooms["room1"]["p2"]):
                        con.send("play")
                elif(quien_ataca == "p2"):
                    if (addr == rooms["room1"]["p3"]):
                        con.send("play")
                elif (quien_ataca == "p3"):
                    if (addr == rooms["room1"]["p4"]):
                        con.send("play")
                elif (quien_ataca == "p4"):
                    if (addr == rooms["room1"]["p1"]):
                        con.send("play")
            # conn.send()
        elif ("S" in data.decode()):
            print("data: {}".format(data.decode()))
            sumar_stringer = data.decode().split()
            jugador_sumar = sumar_stringer[2]
            if(jugador_sumar == "p1"):
                print("add to p1")
                puntaje_p1 = puntaje_p1 + sumar_stringer[1]
                con.send(str(puntaje_p1).encode())
                con.sendall("p2".encode())
            elif (jugador_sumar == "p2"):
                print("add to p2")
                puntaje_p2 = puntaje_p2 + sumar_stringer[1]
                con.send(str(puntaje_p2).encode())
                con.sendall("p3".encode())
            elif (jugador_sumar == "p3"):
                print("add to p3")
                puntaje_p3 = puntaje_p3 + sumar_stringer[1]
                con.send(str(puntaje_p3).encode())
                con.sendall("p4".encode())
            elif (jugador_sumar == "p4"):
                print("add to p4")
                puntaje_p4 = puntaje_p4 + sumar_stringer[1]
                con.send(str(puntaje_p4).encode())
                con.sendall("p1".encode())

            #puntaje_p1 = puntaje_p1 + int(data.decode())
        elif ("R" in data.decode()):
            robo = data.decode().split()
            usuario_que_roba = robo[1]
            robado = robo[2]
            carta_robada = robo[3]
            # enviar al jugador correspondiente determinar exito o fracaso y reenviar al jugador inicial
            if(addr == rooms["room1"][robado]):
                a_robar = usuario_que_roba + " " + carta_robada
                con.send(a_robar.encode())
        elif ("exito" in data.decode()):
            exito = data.decode.split()
            player_exito = exito[0]
            if(addr == rooms["room1"][player_exito]):
                con.send("play")
                if (rooms["room1"][player_exito] == "p1"):
                    if (addr == rooms["room1"]["p2"]):
                        con.send("play")
                elif (rooms["room1"][player_exito] == "p2"):
                    if (addr == rooms["room1"]["p3"]):
                        con.send("play")
                elif (rooms["room1"][player_exito] == "p3"):
                    if (addr == rooms["room1"]["p4"]):
                        con.send("play")
                elif (rooms["room1"][player_exito] == "p4"):
                    if (addr == rooms["room1"]["p1"]):
                        con.send("play")

        elif("fallo" in data.decode()):
            fallo = data.decode()
            player_fallo = fallo[0]
            if (addr == rooms["room1"][player_fallo]):
                con.send("discard")
        elif(data.decode() == "lista"):
            for i in range(len(adresses)):
                adress = adresses[i]
                adress_response = "address: " + str(adress)
                con.send(adress_response.encode())
        elif("join" in data.decode()):
            join_room = data.decode().split()
            the_room = join_room[1]
            if(rooms["room1"]["count"] < 4 and the_room == rooms["room1"]["pin"]):
                rooms["room1"][players.pop(randint(0, len(players)-1))] = addr[1]
                con.send(b'joined room successfully')
                rooms["room1"]["count"] = rooms["room1"]["count"] + 1
                print(rooms["room1"])
            elif(rooms["room2"]["count"] < 4 and the_room == rooms["room2"]["pin"]):
                rooms["room2"][players2.pop(randint(0, len(players2)-1))] = addr[1]
                con.send(b'joined room2 successfully')
                rooms["room2"]["count"] = rooms["room2"]["count"] + 1
                print(rooms["room2"])
            else:
                con.send(b'room is full')
        elif("nombre" in data.decode()):
            nickname = data.decode().split()
            clients[addr[1]] = nickname[1]
            print("El nombre es", nickname[1] )
        elif("chat" in data.decode()):
            con.sendall(data)



def threaded_read(con):
    data = con.recv(1024)
    return data

#def threaded_write(con,msg):
    #con.send(msg)
def Main():
    #global p1_cards, p2_cards, p3_cards, p4_cards
    repartir_cartas()
    HOST = '127.0.0.1'
    PORT = 65432

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("socket binded to port", PORT)
    s.listen(5)
    while True:
        # establish connection with client
        con, addr = s.accept()
        #s.setblocking(0)
        # lock acquired by client
        #some_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
        if addr[1] not in adresses:
            adresses.append(addr[1])
            clients[addr[1]] = ''

        # Start a new thread and return its identifier
        #t1 = threading.Thread(target=threaded_server(con, addr))
        #t2 = threading.Thread(target= threaded_read(con))
        #t1.start()
        #t2.start()
        start_new_thread(threaded_server, (con, addr))
    #s.close()


def repartir_cartas():
    #global p1_cards, p2_cards, p3_cards, p4_cards
    palo = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    baraja = palo + palo + palo + palo
    for i in range(13):
        p1_cards.append(baraja.pop(randint(0, len(baraja) - 1)))
        p2_cards.append(baraja.pop(randint(0, len(baraja) - 1)))
        p3_cards.append(baraja.pop(randint(0, len(baraja) - 1)))
        p4_cards.append(baraja.pop(randint(0, len(baraja) - 1)))


def obtener_nombres_jugadores():
    names = []
    for direccion in clients.values():
        names.append(direccion)
    return names




def ready_to_play(con,addr):
    print("ready to play")
    #p1_cards, p2_cards, p3_cards, p4_cards = repartir_cartas()
    if(addr == rooms["room1"]["p1"]):
        separator = ","
        send_cards_p1 = separator.join(p1_cards)
        names = obtener_nombres_jugadores()
        names_instr = ",".join(names)
        final_msg = names_instr + " " + send_cards_p1
        con.send(final_msg.encode())
    elif(addr == rooms["room1"]["p2"]):
        separator = ","
        send_cards_p2 = separator.join(p2_cards)
        names = obtener_nombres_jugadores()
        names_instr = ",".join(names)
        final_msg = names_instr + " " + send_cards_p2
        con.send(final_msg.encode())
    elif (addr == rooms["room1"]["p3"]):
        separator = ","
        send_cards_p3 = separator.join(p3_cards)
        names = obtener_nombres_jugadores()
        names_instr = ",".join(names)
        final_msg = names_instr + " " + send_cards_p3
        con.send(final_msg.encode())
    elif (addr == rooms["room1"]["p4"]):
        separator = ","
        send_cards_p4 = separator.join(p4_cards)
        names = obtener_nombres_jugadores()
        names_instr = ",".join(names)
        final_msg = names_instr + " " + send_cards_p4
        con.send(final_msg.encode())
    else:
        print("los anteriores no funcian")
        all_cards = p1_cards + p2_cards + p3_cards + p4_cards
        all_cards = ",".join(all_cards)
        names = obtener_nombres_jugadores()
        names_instr = ",".join(names)
        final_msg = names_instr + " " + all_cards
        con.sendall(final_msg.encode())


if __name__ == '__main__':
    Main()