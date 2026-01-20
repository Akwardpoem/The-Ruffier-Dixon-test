# напиши модуль для реализации секундомера
from kivy.clock import Clock
from kivy.properties import BooleanProperty
from kivy.uix.label import Label

class Seconds(Label):

    done = BooleanProperty(False)

    def __init__(self, total,text,color, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        my_text = text
        self.color = color
        super().__init__(text=my_text,color=self.color)

    def start(self):
        Clock.schedule_interval(self.change, 1.5)

    def change(self, dt):
        self.current += 1
        self.text = 'Приседаний осталось: ' + str(self.total - self.current)
        if self.current >= self.total:
            self.done = True
            return False