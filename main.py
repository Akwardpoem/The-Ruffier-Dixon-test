from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.image import Image

Window.size = (400, 300)
Window.clearcolor = (27/256,139/256,225/256,1)

dark_blue = (60/256,81/256,97/256,0.88)

class PracticeColors(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        label = AnimatedText(text='[b]' + '''В этом коде собраны виджеты, на\nкоторых можно попрактиковаться в\nиспользовании новых инструментов. Попробуй\nизменить цвет этого Label, поработай\nс TextInput и кнопкой.'''+ '[/b]', size_hint=(1, 1), markup=True)
        layout.add_widget(label)

        text_input = TextInput(foreground_color=(1,1,1,1),size_hint=(1,0.5),cursor_color=(1,1,1,1))
        text_input.background_color =dark_blue
        layout.add_widget(text_input)
    
        button = Button(text="Отправить",size_hint=(1,0.5))
        button.background_color = dark_blue
        button.on_press = label.start_animation
        layout.add_widget(button)

        image = Image(source='12343.png')
        layout.add_widget(image)

        return layout
    
class AnimatedText(Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        startcolor = self.color
        startfont = self.font_size

        animate = Animation(color=(0,0,0,1), duration=0.5)
        animate += Animation(font_size=5)
        animate += Animation(color=(0.5,0.5,0.5,1),duration=0.3)
        animate += Animation(font_size = 40)
        animate += Animation(color=(1,1,1,1))
        back = Animation(color = startcolor, font_size=startfont)

        self.animate = animate + back
    
    def start_animation(self):
        self.animate.start(self)

PracticeColors().run()