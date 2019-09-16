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
#Config.set('graphics', 'width', 400)

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



class Crear(Screen):
    def __init__(self,**Kwargs):
        super(Crear, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget


#Esta pantalla se muestra si:
#    -El PIN de la sala no existe
#    -La sala esta llena
class NoEntrar(Screen):
    def __init__(self,**Kwargs):
        super(NoEntrar, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget


class Juego(Screen):
    def __init__(self,**Kwargs):
        super(Juego, self).__init__(**Kwargs)
        self.orientation = "vertical"
        S = Image(source='imagenes/fondoRojo.jpeg', allow_stretch=True)
        self.add_widget(S) #añade la imagen al widget



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
