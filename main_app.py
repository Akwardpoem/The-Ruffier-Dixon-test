# напиши здесь свое приложение
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.properties import BooleanProperty
from ruffier import *
from seconds import *
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.progressbar import ProgressBar

name = ''
age = ''
result1 = ''
result2 = ''
result3 = ''

BEIGE = (255/256, 245/256, 207/256, 1)
BLACK = (0,0,0,1)
WHITE = (1,1,1,1)
BLUE = (50/256,57/256,118/256,1)

image_source = '1234.png'


class Main_screen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical',spacing=15)
        name_layout = BoxLayout(size_hint=(0.5,None),height='30sp',pos_hint={'center_x': 0.48, 'center_y': 0.5})
        age_layout = BoxLayout(size_hint=(0.5,None),height='30sp',pos_hint={'center_x': 0.48, 'center_y': 0.5})

        image = Image(source=image_source)

        title = Label(color=BLACK,text='[size=35]'+'[b]'+'Тест Руфье'+'[/b]'+'[/size]',markup=True)

        txt_instruction = Label(color=BLACK,text='Данное приложение позволит вам с помощью теста Руфье \n провести первичную диагностику вашего здоровья.\nПроба Руфье представляет собой нагрузочный комплекс, \n предназначенный для оценки работоспособности сердца при физической нагрузке.\nУ испытуемого определяют частоту пульса за 15 секунд.\nЗатем в течение 45 секунд испытуемый выполняет 30 приседаний.\nПосле окончания нагрузки пульс подсчитывается вновь: \nчисло пульсаций за первые 15 секунд, 30 секунд отдыха,\n число пульсаций за последние 15 секунд.\n')
        
        self.name_text = TextInput(multiline=False,hint_text='Введите имя')
        name_label = Label(text='Ваше имя:',color=BLACK)
        

        self.age_text = TextInput(multiline=False,hint_text='Введите возраст')
        age_label = Label(text='Ваш возраст:',color=BLACK)
        

        self.button = Button(text='Начать',size_hint=(0.4,None),size=(0,40),pos_hint={'center_x': 0.5, 'center_y': 0.5},color=WHITE,background_color=BLUE)
        self.button.on_press = self.next

        name_layout.add_widget(name_label)
        name_layout.add_widget(self.name_text)

        age_layout.add_widget(age_label)
        age_layout.add_widget(self.age_text)

        main_layout.add_widget(image)
        main_layout.add_widget(title)
        main_layout.add_widget(txt_instruction)
        main_layout.add_widget(name_layout)
        main_layout.add_widget(age_layout)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        global name, age
        name = self.name_text.text
        age = self.age_text.text
        try:
            age = int(age)
            self.manager.current = 'second'
        except:
            self.age_text.text = 'Введите целое число'
            self.age_text.text = ''
            self.age_text.hint_text = 'Введите целое число'


class Second_screen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical',spacing=15)
        res_layout = BoxLayout(size_hint=(0.8,None),height='30sp',spacing=15)
        squat_layout = BoxLayout(size_hint=(1,0.6))

        self.timer_label = Seconds(2,text='Замерьте пульс за 15 секунд.\nРезультат запишите в соответствующее поле.',color=BLACK)
        self.timer_label.bind(done=self.sec_finished)

        self.squatbutton = SquatButton(steptime=1.5,repeat=True,text='Приседание',size_hint=(0.4,None),height = 30,pos_hint={'center_x': 0.5, 'center_y': 0.5,'top':-0.3},size=(0,40),color=WHITE,background_color=BLUE,)
        
        self.result_text = TextInput(multiline=False,disabled=True)
        result_label = Label(text='Ваш результат:',color=BLACK)
        
        self.button = Button(text='Старт',size_hint=(0.4,None),height = 30,pos_hint={'center_x': 0.5, 'center_y': 0.5},size=(0,40),color=WHITE,background_color=BLUE)
        self.button.bind(on_press=self.start_timer)
        self.button.on_press = self.next

        res_layout.add_widget(result_label)
        res_layout.add_widget(self.result_text)

        squat_layout.add_widget(self.timer_label)
        squat_layout.add_widget(self.squatbutton)

        main_layout.add_widget(squat_layout)
        main_layout.add_widget(res_layout)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)
    
    def start_timer(self, *args):
        self.squatbutton.start_animation()
        self.squatbutton.animate.repeat = True
        self.squatbutton.finish = False

        self.button.text = 'Продолжить'
        self.button.disabled = True
        self.timer_label.start()

    def sec_finished(self, *args):
        if self.timer_label.done:
            self.timer_label.text = 'Таймер завершён!'
            self.squatbutton.animate.repeat = False
            self.result_text.disabled = False
            self.button.disabled = False

    def next(self):
        global result1
        result1 = self.result_text.text
        try:
            result1 = int(result1)
            self.manager.current = 'third'
        except:
            self.result_text.text = ''
            self.result_text.hint_text = 'Введите целое число'


class Third_screen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical',spacing=15)
        name_layout = BoxLayout(size_hint=(0.8,None),height='30sp',spacing=15)
        age_layout = BoxLayout(size_hint=(0.8,None),height='30sp',spacing=15)

        txt_instruction = Label(text='В течение минуты замерьте пульс два раза:\nза первые 15 секунд минуты, затем за последние 15 секунд.\nРезультаты запишите в соответствующие поля.',color=BLACK)
        
        self.first_text = TextInput(multiline=False)
        first_label = Label(text='Результат:',color=BLACK)

        self.second_text = TextInput(multiline=False)
        second_label = Label(text='Результат после отдыха:',color=BLACK)

        self.button = Button(text='Завершить',size_hint=(0.4,None),height = 30,pos_hint={'center_x': 0.5, 'center_y': 0.5},size=(0,40),color=WHITE,background_color=BLUE)
        self.button.on_press = self.next

        name_layout.add_widget(first_label)
        name_layout.add_widget(self.first_text)

        age_layout.add_widget(second_label)
        age_layout.add_widget(self.second_text)

        main_layout.add_widget(txt_instruction)
        main_layout.add_widget(name_layout)
        main_layout.add_widget(age_layout)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        global result2, result3
        result2 = self.first_text.text
        result3 = self.second_text.text
        try:
            result2 = int(result2)
            try:
                result3 = int(result3)
                self.manager.current = 'fourth'
            except:
                self.second_text.text = ''
                self.second_text.hint_text = 'Введите целое число'
        except:
            self.first_text.text = ''
            self.first_text.hint_text = 'Введите целое число'


class Fourth_screen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.text = Label(text='',color=BLACK)
        self.pb = Counter(max=100, value=0)
        layout.add_widget(self.pb)
        layout.add_widget(self.text)
        self.add_widget(layout)
        self.on_enter = self.pb.start_animation
        self.pb.animate.on_complete = self.new
    
    def new(self):
        self.text.text=str(test(result1,result2,result3,age))


class ScrButton(Button):
    def __init__(self,scr,direction='right',goal='main',**kwargs):
        super().__init__(**kwargs)
        self.scr = scr
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.scr.manager.transition.direction = self.direction
        self.scr.manager.current = self.goal


class My_app(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main_screen(name='main'))
        sm.add_widget(Second_screen(name='second'))
        sm.add_widget(Third_screen(name='third'))
        sm.add_widget(Fourth_screen(name='fourth'))
        return sm
    

class SquatButton(Button):
    def __init__(self,steptime,repeat,**kwargs):
        self.animate = Animation(pos_hint={'top':0.3},duration=steptime/2)
        self.animate += Animation(pos_hint={'top':-0.3},duration=steptime/2)
        self.animate.repeat = repeat
        super().__init__(**kwargs)

    def start_animation(self):
        self.animate.start(self)


class Counter(ProgressBar):
    def __init__(self,**kwargs):
        self.animate = Animation(value=20,duration=0.5)
        self.animate += Animation(value=80,duration=1)
        self.animate += Animation(value=100,duration=0.1)
        super().__init__(**kwargs)
    def start_animation(self):
        self.animate.start(self)
     
Window.clearcolor = BEIGE

My_app().run()




