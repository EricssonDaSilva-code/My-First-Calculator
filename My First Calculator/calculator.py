from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_file('./caculator.kv')
Window.size = (350, 550)
class CalculatorWidget(Widget):

    def clear(self):
        self.ids.input_box.text = '0'

    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if 'wrong equation' in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f'{number}'
        else:
            self.ids.input_box.text = f'{prev_number}{number}'

    def signs(self, sign):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f'{prev_number}{sign}'
        if len(self.ids.input_box.text) >= 3:
            if self.ids.input_box.text[-2].isnumeric():
                pass
            elif '+' or '-' or '/' or '*' or '%' in self.ids.input_box.text[-2]:
                pos2 = self.ids.input_box.text[-2]
                pos1 = self.ids.input_box.text[-1]
                prev_number = self.ids.input_box.text[:-2]
                self.ids.input_box.text = f'{prev_number}{pos1}'


    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    def result(self):
        prev_number = self.ids.input_box.text
        try:
            result = eval(prev_number)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = 'wrong equation'

    def positive_negative(self):
        prev_number = self.ids.input_box.text

        if '-' in prev_number:
            self.ids.input_box.text = f'{prev_number.replace("-", "")}'
        else:
            self.ids.input_box.text = f"-{prev_number}"

    def dot(self):
        prev_number = self.ids.input_box.text
        num_list = re.split('\+|-|\*|/|%', prev_number)

        if ('+' in prev_number or '-' in prev_number or '*' in prev_number or '/' in prev_number
        or '%' in prev_number) and '.' not in num_list[-1]:
            prev_number = f'{prev_number}.'
            self.ids.input_box.text = prev_number

        elif '.' in prev_number:
            pass
        else:
            prev_number = f'{prev_number}.'
            self.ids.input_box.text = prev_number

    def per_cent(self):
        prev_number = self.ids.input_box.text
        a = prev_number.rfind('+')
        b = prev_number.rfind('-')
        c = prev_number.rfind('*')
        d = prev_number.rfind('/')
        e = a, b, c, d
        biggest_sign = sorted(e)[3]
        account = prev_number[:biggest_sign]
        last_sign = prev_number[biggest_sign]
        account_percent = prev_number[biggest_sign+1:]
        account_resolved = int(eval(account))
        cent = int(account_percent) / 100
        percent = cent * account_resolved
        self.ids.input_box.text = f'{account_resolved}{last_sign}{percent}'






class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()


