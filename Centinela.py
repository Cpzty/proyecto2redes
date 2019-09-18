import time
import socket
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from  kivy.uix.floatlayout import FloatLayout
import kivy.core.text.markup
import kivy.resources
from kivy.graphics import Color, Rectangle ,Line
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup


Config.set('graphics', 'resizable', 'False')

class Variables():
    def __init__(self):
        self.player_name = ""
        self.num = ""

    def setplayer_name(self, nuevo):
        self.player_name = nuevo
    
    def getplayer_name(self):
        return self.player_name
    
    def setnum(self, nuevo):
        self.num = nuevo
    
    def getnum(self):
        return self.num

class Contenedor(BoxLayout):
    None

class Name(Screen):
    def __init__(self,**Kwargs):
        super(Name, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget
        my_box1 = FloatLayout(size=(300, 300))
        #titulo 
        my_label1 = Label(text='[color=ffffff][b] Centinela [/b][/color]', markup = True, font_size = "70dp", font_name= "Times",size_hint=(0.3, 0.3), pos=(150, 420))
        #label nombre
        my_label2 = Label(text='[color=ffffff]  Escriba el nombre de usuario: [/color]', markup = True, font_size = "40dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(200, 250))
        #input nombre
        self.my_input = TextInput(size_hint=(0.3, 0.1), pos=(130, 230))
        #Boton para ingresar al programa
        btn = Button(text= "Inicio", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(350,120))
        btn.bind(on_press = self.changer)
        btnHelp = Button(font_size=24, size_hint=(0.09, 0.1), pos=(600,500))
        btnHelp.bind(on_press = self.changerHelp)
        btnHelp.add_widget(Image(source='imagenes/help.jpg', pos=(600,500), allow_stretch=True))
        my_box1.add_widget(my_label1)
        my_box1.add_widget(my_label2)
        my_box1.add_widget(self.my_input)
        my_box1.add_widget(btn)
        my_box1.add_widget(btnHelp)
        self.add_widget(my_box1)

    def changer(self, btn): #Cambiar de pantalla 
        self.manager.current = "Salas"
        varg.setplayer_name(self.my_input.text)
        name = "nombre "+varg.getplayer_name()
        print(name)
        s.sendall(name.encode())

    def changerHelp(self, btn): #Cambiar de pantalla 
        self.manager.current = "Salas"

class Salas(Screen):
    def __init__(self,**Kwargs):
        super(Salas, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget
        my_box1 = FloatLayout(size=(300, 300))
        btnEntrar = Button(text= "Entrar a una sala", size_hint=(.3, .1), font_size=24, background_color = [0, 1, 0.6, 0.8], pos=(150,300))
        btnEntrar.bind(on_press = self.changerEntrar)
        btnCrear = Button(text= "Crear una sala", size_hint=(.3, .1), font_size=24, background_color = [0, 1, 0.6, 0.8], pos=(150,200))
        btnCrear.bind(on_press = self.changerCrear)
        my_box1.add_widget(btnEntrar)
        my_box1.add_widget(btnCrear)
        self.add_widget(my_box1)

    def changerEntrar(self, btn): #Cambiar de pantalla 
        self.manager.current = "Entrar"
    
    def changerCrear(self, btn): #Cambiar de pantalla 
        self.manager.current = "Crear"

class Entrar(Screen):
    def __init__(self,**Kwargs):
        super(Entrar, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget

        self.my_box1 = FloatLayout(size=(300, 300))
        # label del PIN
        self.my_label = Label(text='[color=ffffff]  Escriba el PIN: [/color]', markup = True, font_size = "40dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(100, 250))
        #input del PIN
        self.pin_input = TextInput(size_hint=(0.3, 0.1), pos=(130, 230))
        #Boton para ingresar al juego
        self.btn = Button(text= "Inicio", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(350,120))
        self.btn.bind(on_press = self.validar)
        self.my_box1.add_widget(self.my_label)
        self.my_box1.add_widget(self.pin_input)
        self.my_box1.add_widget(self.btn)
        self.add_widget(self.my_box1)

    def validar(self,btn):
        self.my_box1.remove_widget(self.btn)
        self.my_box1.remove_widget(self.my_label)
        self.my_box1.remove_widget(self.pin_input)
        my_label2 = Label(text='[color=ffffff]  Esperando... [/color]', markup = True, font_size = "40dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(150, 100))
        self.my_box1.add_widget(my_label2)
        num = self.pin_input.text
        join = "join "+num
        s.sendall(join.encode())
        message = s.recv(1024).decode()
        print(message)
        if(message == "joined room successfully"):
            esperando = True
            while (esperando == True):
                time.sleep(10)
                s.sendall(b'sala')
                a = s.recv(1024).decode()
                if (a != "no"):
                    print(a)
                    esperando = False
                
        else:
            self.changerNoEntrar()

    def changerJuego(self, btn): #Cambiar de pantalla 
        #varg.setnum(num)
        self.manager.current = "Juego"

    def changerNoEntrar(self): #Cambiar de pantalla 
        self.manager.current = "NoEntrar"

class Espera(Screen):
    def __init__(self,**Kwargs):
        super(Espera, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget
        my_box = FloatLayout(size=(300, 300))
        my_label = Label(text='[color=ffffff]  Esperando que se unan todos los \n jugadores a la sala: [/color]'+varg.num, markup = True, font_size = "40dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(100, 150))
        my_box.add_widget(my_label)

class Crear(Screen):
    def __init__(self,**Kwargs):
        super(Crear, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget

        self.my_box1 = FloatLayout(size=(300, 300))
        # label del PIN
        self.btnPin = Button(text= "Generar PIN", font_size=24, size_hint=(0.3, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(250,350))
        self.btnPin.bind(on_press= self.generarPin)
        #Boton para ingresar al juego
        self.btn = Button(text= "Inicio", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(350,120))
        self.btn.bind(on_press = self.changerJuego)
        self.my_box1.add_widget(self.btn)
        self.my_box1.add_widget(self.btnPin)
        self.add_widget(self.my_box1)

    def generarPin(self, btn):
        s.sendall(b'PIN')
        num = s.recv(1024).decode() # reemplazar por el numero de sala
        varg.setnum(num)
        my_label = Label(text='[color=ffffff]  El PIN es: [/color]'+varg.getnum(), markup = True, font_size = "40dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(100, 150))
        self.my_box1.add_widget(my_label)       

    def changerJuego(self, btn): #Cambiar de pantalla
        self.my_box1.remove_widget(self.btn)
        self.my_box1.remove_widget(self.btnPin)
        my_label = Label(text='[color=ffffff]  Esperando... [/color]', markup = True, font_size = "40dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(150, 100))
        self.my_box1.add_widget(my_label)
        join = "join "+ varg.getnum()
        s.sendall(join.encode())
        print(varg.getnum())
        message = s.recv(1024).decode()
        print(message)
        if(message == "joined room successfully"):
            esperando = True
            while (esperando == True):
                time.sleep(25)
                s.sendall(b'sala')
                a = s.recv(1024).decode()
                if (a != "no"):
                    print(a)
                    esperando = False
            
            
        #   TODO: Preguntar al server cuando ya se pueda entrar
        # nombres de los jugadores
        # cartas del jugador
        #while ( s.recv(1024).decode() == ""):
         #   pass
        #self.manager.current = "Juego"
    
    

#Esta pantalla se muestra si:
#    -El PIN de la sala no existe
#    -La sala esta llena
class NoEntrar(Screen):
    def __init__(self,**Kwargs):
        super(NoEntrar, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget
        
        my_box1 = FloatLayout(size=(300, 300))
        # label del PIN
        my_label = Label(text='[color=ffffff] El PIN de la sala no existe o \n La sala esta llena [/color]', markup = True, font_size = "40dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(200, 250))
        #Boton para ingresar al juego
        btn = Button(text= "Regresar", font_size=24, size_hint=(0.2, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(150,170))
        btn.bind(on_press = self.changer)
        my_box1.add_widget(my_label)
        my_box1.add_widget(btn)
        self.add_widget(my_box1)

    def changer(self, btn): #Cambiar de pantalla 
        self.manager.current = "Salas"

class Juego(Screen):
    def __init__(self,**Kwargs):
        super(Juego, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/juego.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget
       

        # Variables
        Turno = "Cristian"
        P1 = "Ana"
        P2 = "Estrella"
        P3 = "Juan"
        Punto = "0"
        Punto1 = "0"
        Punto2 = "0"
        Punto3 = "0"
        self.option = ""
        self.botones = []

        self.my_box1 = FloatLayout(size=(300, 300))
        labelTitle = Label(text='[color=000000] CENTINELA [/color]', markup = True, font_size = "70dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(120, 450))
        labelChat = Label(text='[color=000000] CHAT [/color]', markup = True, font_size = "50dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(500, 450))
        
        
        SP1 = Image(source='imagenes/moneda.png', size_hint=(0.2, 0.1), pos=(30, 370) )
        SP2 = Image(source='imagenes/moneda.png', size_hint=(0.2, 0.1), pos=(150, 370) )
        SP3 = Image(source='imagenes/moneda.png', size_hint=(0.2, 0.1), pos=(270, 370) )
        labelPunto1 = Label(text='[color=000000] '+Punto1+'[/color]', markup = True, font_size = "30dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(55, 350))
        labelPunto2 = Label(text='[color=000000] '+Punto2+'[/color]', markup = True, font_size = "30dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(175, 350))
        labelPunto3 = Label(text='[color=000000] '+Punto3+'[/color]', markup = True, font_size = "30dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(295, 350))
        
        labelP1 = Label(text='[color=165B03] '+P1+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(-20, 270))
        labelP2 = Label(text='[color=165B03] '+P2+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(110, 270))
        labelP3 = Label(text='[color=165B03] '+P3+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(220, 270))
        
        #Acción de atacar
        self.btnIniciar = Button(text= "INICIAR", font_size=85, size_hint=(0.5, 0.5), background_color = [0, 166, 0, 38], pos=(100,30))
        self.btnIniciar.bind(on_press = self.iniciar)

        #Acción de atacar
        self.btnAtacar = Button(text= "Atacar", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(100,10))
        self.btnAtacar.bind(on_press = self.changerAR)
        #Acción de sumar
        self.btnSumar = Button(text= "Sumar", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(200,10))
        self.btnSumar.bind(on_press = self.changer)
        #Acción de Robar
        self.btnRobar = Button(text= "Robar", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(300,10))
        self.btnRobar.bind(on_press = self.changerAR)

        labelPunto = Label(text='[color=000000] '+Punto+'[/color]', markup = True, font_size = "30dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(375, -10))
        puntosImg = Image(source='imagenes/moneda.png', size_hint=(0.2, 0.1), pos=(350, 10) )

        #Chat
        messageInput = TextInput(size_hint=(0.2, 0.1), pos=(550, 10))
        #Boton para enviar mensaje
        btn = Button(text= "Enviar", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(720,10))
        btn.bind(on_press = self.changer)
        
        self.my_box1.add_widget(labelTitle)
        self.my_box1.add_widget(labelChat)
        self.my_box1.add_widget(messageInput)
        self.my_box1.add_widget(SP1)
        self.my_box1.add_widget(SP2)
        self.my_box1.add_widget(SP3)
        self.my_box1.add_widget(labelP1)
        self.my_box1.add_widget(labelP2)
        self.my_box1.add_widget(labelP3)
        puntosImg.add_widget(labelPunto)
        puntosImg.add_widget(labelPunto1)
        puntosImg.add_widget(labelPunto2)
        puntosImg.add_widget(labelPunto3)
        self.my_box1.add_widget(btn)
        self.my_box1.add_widget(self.btnAtacar)
        self.my_box1.add_widget(self.btnRobar)
        self.my_box1.add_widget(self.btnSumar)            
        self.my_box1.add_widget(puntosImg)
        self.my_box1.add_widget(self.btnIniciar)  
        self.add_widget(self.my_box1)

    
        

    def jugada(self, btn):
        for a in self.botones:
            self.my_box1.remove_widget(a) 
        self.my_box1.add_widget(self.btnAtacar)
        self.my_box1.add_widget(self.btnRobar)
        self.my_box1.add_widget(self.btnSumar) 

    def generarCartas(self):
        #peticion de mis cartas al server
        cartas = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
        x = 30
        y = 100
        cont = 0
        
        for a in cartas:
            self.btnC = Button(text= a, font_size=24, size_hint=(0.05, 0.08), background_color = [0, 1, 0.6, 0.8], pos=(x,y))
            self.btnC.bind(on_press = self.jugada)
            self.my_box1.add_widget(self.btnC) 
            self.botones.append(self.btnC)
            cont = cont + 1
            if (cont < 7):    
                x = x + 50
            elif(cont == 7):
                y = 50
                x = 30
            else:
                x = x + 50 
         

    def iniciar(self, btn):
        self.my_box1.remove_widget(self.btnIniciar) 
        labelPin = Label(text='[color=165B03] Estas en la sala: '+varg.getnum()+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(120, 400))
        labelTurno = Label(text='[color=165B03] Es turno de: '+varg.getplayer_name()+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(120, 380))
        self.my_box1.add_widget(labelPin)
        self.my_box1.add_widget(labelTurno)      

    def cartas(self):
        if (self.option == "AR"):
            self.my_box1.remove_widget(self.btnCon) 
            self.my_box1.remove_widget(self.Jugador) 
            self.my_box1.remove_widget(self.labelJ) 

        self.generarCartas()

    def changerAR(self, btn): #Cambiar de pantalla 
        self.option = "AR"
        self.my_box1.remove_widget(self.btnAtacar)
        self.my_box1.remove_widget(self.btnRobar)
        self.my_box1.remove_widget(self.btnSumar) 

        self.labelJ = Label(text='[color=165B03] Jugador: [/color]', markup = True, font_size = "30dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(10, 10))
        self.my_box1.add_widget(self.labelJ)
        self.Jugador = TextInput(size_hint=(0.2, 0.1), pos=(40, 10))
        self.btnCon = Button(text= "continuar", font_size=24, size_hint=(0.17, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(210,15))
        self.btnCon.bind(on_press = self.change)
        self.my_box1.add_widget(self.btnCon) 
        self.my_box1.add_widget(self.Jugador) 
    
    def change(self, btn):
        self.cartas()

    def changer(self, btn): #Cambiar de pantalla 
        self.my_box1.remove_widget(self.btnAtacar)
        self.my_box1.remove_widget(self.btnRobar)
        self.my_box1.remove_widget(self.btnSumar) 
        self.cartas()

class CentinelaApp(App):
    
    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = Name(name = "Name")
        screen2 = Salas(name = "Salas")
        screen3 = Entrar(name = "Entrar")
        screen4 = Crear(name = "Crear")
        screen5 = NoEntrar(name = "NoEntrar")
        screen6 = Juego(name = "Juego")
        screen7 = Juego(name = "Espera")
    
        my_screenmanager.add_widget(screen1)
        my_screenmanager.add_widget(screen2)
        my_screenmanager.add_widget(screen3)
        my_screenmanager.add_widget(screen4)
        my_screenmanager.add_widget(screen5)
        my_screenmanager.add_widget(screen6)
        my_screenmanager.add_widget(screen7)
        
        return my_screenmanager        

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 65432
    varg = Variables()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        CentinelaApp().run()
