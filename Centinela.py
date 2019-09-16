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

Config.set('graphics', 'resizable', 'False')

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
        my_input = TextInput(size_hint=(0.3, 0.1), pos=(130, 230))
        #Boton para ingresar al programa
        btn = Button(text= "Inicio", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(350,120))
        btn.bind(on_press = self.changer)
        my_box1.add_widget(my_label1)
        my_box1.add_widget(my_label2)
        my_box1.add_widget(my_input)
        my_box1.add_widget(btn)
        self.add_widget(my_box1)

    def changer(self, btn): #Cambiar de pantalla 
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

        my_box1 = FloatLayout(size=(300, 300))
        # label del PIN
        my_label = Label(text='[color=ffffff]  Escriba el PIN: [/color]', markup = True, font_size = "40dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(100, 250))
        #input del PIN
        pin_input = TextInput(size_hint=(0.3, 0.1), pos=(130, 230))
        #Boton para ingresar al juego
        btn = Button(text= "Inicio", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(350,120))
        print(pin_input.text)
        if(pin_input.text == "hola"):
            btn.bind(on_press = self.changerJuego)
        else:
            btn.bind(on_press = self.changerNoEntrar)
        my_box1.add_widget(my_label)
        my_box1.add_widget(pin_input)
        my_box1.add_widget(btn)
        self.add_widget(my_box1)

    def changerJuego(self, btn): #Cambiar de pantalla 
        self.manager.current = "Juego"

    def changerNoEntrar(self, btn): #Cambiar de pantalla 
        self.manager.current = "NoEntrar"

class Crear(Screen):
    def __init__(self,**Kwargs):
        super(Crear, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget

        my_box1 = FloatLayout(size=(300, 300))
        # label del PIN
        btnPin = Button(text= "Generar PIN", font_size=24, size_hint=(0.3, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(250,350))
        btnPin.bind(on_press= self.generarPin)
        #Boton para ingresar al juego
        btn = Button(text= "Inicio", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(350,120))
        btn.bind(on_press = self.changerJuego)
        my_box1.add_widget(btn)
        my_box1.add_widget(btnPin)
        self.add_widget(my_box1)

    def changerJuego(self, btn): #Cambiar de pantalla 
        self.manager.current = "Juego"
    
    def generarPin(self, btn):
        num = "34"  # reemplazar por el numero de sala
        my_box = FloatLayout(size=(300, 300))
        my_label = Label(text='[color=ffffff]  El PIN es: [/color]'+num, markup = True, font_size = "40dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(100, 150))
        my_box.add_widget(my_label)
        self.add_widget(my_box)

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
        PIN = "34"
        Turno = "Cristian"
        P1 = "Ana"
        P2 = "Estrella"
        P3 = "Juan"

        my_box1 = FloatLayout(size=(300, 300))
        labelTitle = Label(text='[color=000000] CENTINELA [/color]', markup = True, font_size = "70dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(120, 450))
        labelChat = Label(text='[color=000000] CHAT [/color]', markup = True, font_size = "50dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(500, 450))
        labelPin = Label(text='[color=165B03] Estas en la sala: '+PIN+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(120, 400))
        labelTurno = Label(text='[color=165B03] Es turno de: '+Turno+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(120, 380))
        SP1 = Image(source='imagenes/moneda.png', size_hint=(0.2, 0.1), pos=(30, 370) )
        SP2 = Image(source='imagenes/moneda.png', size_hint=(0.2, 0.1), pos=(150, 370) )
        SP3 = Image(source='imagenes/cartas.png', size_hint=(0.2, 0.1), pos=(270, 370) )
        labelP1 = Label(text='[color=165B03] '+P1+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(-20, 270))
        labelP2 = Label(text='[color=165B03] '+P2+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(110, 270))
        labelP3 = Label(text='[color=165B03] '+P3+'[/color]', markup = True, font_size = "20dp", font_name= "Times", size_hint=(0.3, 0.3), pos=(220, 270))


        #Acción de atacar
        btnAtacar = Button(text= "Atacar", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(100,10))
        btnAtacar.bind(on_press = self.changer)
        #Acción de sumar
        btnSumar = Button(text= "Sumar", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(200,10))
        btnSumar.bind(on_press = self.changer)
        #Acción de Robar
        btnRobar = Button(text= "Robar", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(300,10))
        btnRobar.bind(on_press = self.changer)
        puntosImg = Image(source='imagenes/moneda.png', size_hint=(0.2, 0.1), pos=(350, 10) )


        #Chat
        messageInput = TextInput(size_hint=(0.2, 0.1), pos=(550, 10))
        #Boton para enviar mensaje
        btn = Button(text= "Enviar", font_size=24, size_hint=(0.1, 0.1), background_color = [0, 1, 0.6, 0.8], pos=(720,10))
        btn.bind(on_press = self.changer)
        
        my_box1.add_widget(labelTitle)
        my_box1.add_widget(labelChat)
        my_box1.add_widget(messageInput)
        my_box1.add_widget(labelPin)
        my_box1.add_widget(labelTurno)
        my_box1.add_widget(SP1)
        my_box1.add_widget(SP2)
        my_box1.add_widget(SP3)
        my_box1.add_widget(labelP1)
        my_box1.add_widget(labelP2)
        my_box1.add_widget(labelP3)
        my_box1.add_widget(btn)
        my_box1.add_widget(btnAtacar)
        my_box1.add_widget(btnRobar)
        my_box1.add_widget(btnSumar)
        my_box1.add_widget(puntosImg)
        self.add_widget(my_box1)

    def changer(self, btn): #Cambiar de pantalla 
        self.manager.current = "Salas"



class CentinelaApp(App):
    
    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = Name(name = "Name")
        screen2 = Salas(name = "Salas")
        screen3 = Entrar(name = "Entrar")
        screen4 = Crear(name = "Crear")
        screen5 = NoEntrar(name = "NoEntrar")
        screen6 = Juego(name = "Juego")
    
        my_screenmanager.add_widget(screen1)
        my_screenmanager.add_widget(screen2)
        my_screenmanager.add_widget(screen3)
        my_screenmanager.add_widget(screen4)
        my_screenmanager.add_widget(screen5)
        my_screenmanager.add_widget(screen6)
        
        return my_screenmanager        

if __name__ == '__main__':
    CentinelaApp().run()
