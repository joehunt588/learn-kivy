
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
import time
import threading
from kivy.properties import StringProperty
# Window.clearcolor = (1,1,1,1)#rgb colour-

class second_item(BoxLayout):
    texts = ObjectProperty(None)
    def prrinte(self):
        print('hello world')
        
    def test_capture_button(self):
        self.ids.k.text = "Boys changed !"# change hello
    def new_main(self):
        print()
    def change_main(self,*arg):
        print(self.texts.text)
        
class main_item(BoxLayout):
    sample = ObjectProperty(None)#connected class for second_item
    texts = ObjectProperty(None)
    def test_capture(self):
        l=Button(text='Hai')
        self.ids.screen_one.add_widget(l)
        self.ids.search_text.text = "Boys changed people!"# change hello
        
    def capture(self):
        print('yes')
       
    def test_capture_2(self): 
        self.ids.hh.text = "Boys changed people good!"# change hello
          
class add_wid(App):
    def build(self):
        pass 
   
    def capture(self):
        print('yes')
if __name__ == '__main__':
    add_wid().run()
