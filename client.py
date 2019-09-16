import socket

HOST = '127.0.0.1'
PORT = 65432

def menu():
    print("Ingrese 1 para mandar un mensaje")
    print("Ingrese 2 para mandar un mensaje estilizado")
    print("Ingrese 3 para salir")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        menu()
        opcion = input(">: ")
        if opcion == str(1):
            s.sendall(b'Hello, world')
        elif opcion == str(2):
            msg_to_send = input("escriba el mensaje: ")
            s.sendall(msg_to_send.encode())
        elif opcion == str(3):
            break
        data = s.recv(1024)
        print('Recibido:', repr(data))
