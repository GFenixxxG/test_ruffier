#Імпорт біблеотек
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from instructions import *
from timer import Timer

Window.clearcolor = (.0, .90, 1, 1)

#Змінні для кольору
lbl_color = (65, 232, 132, 1)
btn_color = (1, .2, .7, 1)

name = ''
age = 0

p1 = 0
p2 = 0
p3 = 0

def cheak_int(str_num):
    try:
        return int(str_num)

    except:
        return False




#Клас для головного екрану
class InstrScr(Screen):
    def __init__(self, **kwargs): # Конструктор
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction, color = lbl_color, bold = True)
        lbl_name = Label(text = "Введіть ім'я:", halign = "right", color = lbl_color, bold = True, font_size = 40)
        self.input_name = TextInput(text = "Ім'я", multiline = False)
        lbl_age = Label(text = "Введіть вік:", halign = "right", color = lbl_color, bold = True, font_size = 40)
        self.input_age = TextInput(text = "7+", multiline = False)
        self.btn = Button(text = "Почати", size_hint = (.3, .2), pos_hint = {"center_x": .5}, bold = True, background_color = btn_color)
        self.btn.on_press = self.next
        #Лінії Горизонтальні
        line1 = BoxLayout(size_hint = (.8, None), height = "30sp")
        line2 = BoxLayout(size_hint = (.8, None), height = "30sp")
        #Додавання віджетів
        line1.add_widget(lbl_name)
        line1.add_widget(self.input_name)
        line2.add_widget(lbl_age)
        line2.add_widget(self.input_age)
        #Додавання віджетів на головну лінію
        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 15)
        main_line.add_widget(instr)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def next(self): #Функція для переходу на наступний екран
        global name, age
        name = self.input_name.text
        age = cheak_int(self.input_age.text)
        if age <= 7 or age == False:
            age = 7
            self.input_age.text = str(age)
        else:
            self.manager.current = 'second'
    
#Клас для другого екрану
class PulseScr(Screen):
        def __init__(self, **kwargs): # Конструктор
            super().__init__(**kwargs) 
            self.next_screen = False

            instr = Label(text = txt_test1, color = lbl_color, bold = True)

            self.lbl_sec = Timer(15, color = lbl_color, bold = True)
            lbl_reslt = Label(text = "Введіть результат:", halign = "right", color = lbl_color, bold = True, font_size = 25)
            self.input_results = TextInput(text = "1", multiline = False)
            self.input_results.set_disabled(True)
            self.btn = Button(text = "Почати", size_hint = (.3, .2), pos_hint = {"center_x": .5}, bold = True, background_color = btn_color)
            self.btn.on_press = self.next

            main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 15)
            main_line.add_widget(instr)
            main_line.add_widget(self.lbl_sec)
            line = BoxLayout(size_hint = (.8, None), height = "30sp")
            line.add_widget(lbl_reslt)
            line.add_widget(self.input_results)
            main_line.add_widget(line)
            main_line.add_widget(self.btn)

            self.add_widget(main_line)
        def next(self): #Функція для переходу на наступний екран
            global p1
            if not self.next_screen:
                self.input_results.set_disabled(False)
                self.lbl_sec.start()
            else:
                p1 = cheak_int(self.input_results.text)
                if p1 <= 0 or p1 == False:
                    p1 = 0
                    self.input_results.text = str(p1)
                else:
                    self.manager.current = 'third'

#Клас для третього екрану
class SitsScr(Screen):
    def __init__(self, **kwargs): # Конструктор
            super().__init__(**kwargs) 
            instr = Label(text = txt_sits, color = lbl_color, bold = True)
            self.sits = Label(text = "Залишилося присідань: 30", color = lbl_color, bold = True)
            self.btn = Button(text = "Почати", size_hint = (.3, .2), pos_hint = {"center_x": .5}, bold = True, background_color = btn_color)
            self.btn.on_press = self.next

            main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 15)
            main_line.add_widget(instr)
            main_line.add_widget(self.sits)
            main_line.add_widget(self.btn)

            self.add_widget(main_line)

    def next(self): #Функція для переходу на наступний екран
        self.manager.current = 'fourth'

#Клас для четвертого екрану
class PulseScrTwo(Screen):
    def __init__(self, **kwargs): # Конструктор
            super().__init__(**kwargs) 
            instr = Label(text = txt_test3, color = lbl_color, bold = True)
            lbl_pulse = Label(text = "Рахуйте пульс", color = lbl_color, bold = True)
            self.lbl_sec = Label(text = "Пройшло секунд: 0", color = lbl_color, bold = True)

            lbl_result = Label(text = "Результат:", halign = "right", color = lbl_color, bold = True, font_size = 40)
            self.input_result = TextInput(text = "0", multiline = False)
            lbl_after_res = Label(text = "Результат після відпочинку:", halign = "right", color = lbl_color, bold = True, font_size = 20)
            self.input_after_res = TextInput(text = "0", multiline = False)

            self.btn = Button(text = "Почати", size_hint = (.3, .2), pos_hint = {"center_x": .5}, bold = True, background_color = btn_color)
            self.btn.on_press = self.next

            main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 15)
            main_line.add_widget(instr)
            main_line.add_widget(lbl_pulse)
            main_line.add_widget(self.lbl_sec)

            line1 = BoxLayout(size_hint = (.8, None), height = "30sp")
            line2 = BoxLayout(size_hint = (.8, None), height = "30sp")

            line1.add_widget(lbl_result)
            line1.add_widget(self.input_result)

            line2.add_widget(lbl_after_res)
            line2.add_widget(self.input_after_res)

            main_line.add_widget(line1)
            main_line.add_widget(line2)

            main_line.add_widget(self.btn)

            self.add_widget(main_line)

    def next(self): #Функція для переходу на наступний екран
        self.manager.current = 'fifth'

#Клас для пятого екрану
class ResultsScr(Screen):
    def __init__(self, **kwargs): # Конструктор
        super().__init__(**kwargs) 
        indx = Label(text = "Ваш індекс Руф'е: ", color = lbl_color, bold = True)
        heart_work = Label(text = "Працездатність сердця: ", color = lbl_color, bold = True)

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 15, size_hint = (.5, .1), pos_hint={'center_x': .5, 'center_y': .5})

        main_line.add_widget(indx)
        main_line.add_widget(heart_work)

        self.add_widget(main_line)

#Клас для приложения
class HeartCheck(App):
    def build(self):
        sm = ScreenManager() # Екрановий менеджер
        #Імена екранів
        sm.add_widget(InstrScr(name = "first"))
        sm.add_widget(PulseScr(name = "second"))
        sm.add_widget(SitsScr(name = "third"))
        sm.add_widget(PulseScrTwo(name = "fourth"))
        sm.add_widget(ResultsScr(name = "fifth"))

        return sm

#Запуск приложухи
app = HeartCheck()
app.run()