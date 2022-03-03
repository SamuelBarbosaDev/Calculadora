



#Como? Criar uma calculadora.

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Calculadora(GridLayout):
    def calcular(self, calculadora):

        try:
            self.display.text = str(eval(calculadora))

        except ZeroDivisionError:
            self.display.text = "Você não pode dividir por zero."

        except SyntaxError:
            self.display.text = ""


class AppCalculadora(App):
    def build(self):
        return Calculadora()

AppCalculadora().run()
