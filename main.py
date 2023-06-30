from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager

class JanelaGerenciadora(ScreenManager):
    pass

class JanelaPrincipal(Screen):
    pass

class JanelaHoras(Screen):
    def calcular(self):
        try:
            tempo = float(self.ids.tempohoras.text)
            volume =float(self.ids.volumehoras.text)
            resultado = (volume) / (3 * tempo)
            resultadomg = resultado * 3
            self.ids.respostahoras.text = '{:.2f} gotas por minuto\n{:.2f} microgotas por minuto'.format(resultado,resultadomg)
        except:
            print('valor invalido')
    def limpar(self):
        self.ids.tempohoras.text=""
        self.ids.volumehoras.text=""
        self.ids.respostahoras.text=""


class JanelaMinutos(Screen):
    def calcular(self):
        try:
            tempo = float(self.ids.tempominutos.text)
            volume = float(self.ids.volumeminutos.text)
            resultado = (volume * 20) / tempo
            resultadomg = resultado * 3
            self.ids.respostaminutos.text = '{:.2f} gotas por minuto\n{:.2f} microgotas por minuto'.format(resultado,resultadomg)
        except:
            print('valor invalido')
    def limpar(self):
        self.ids.tempominutos.text=""
        self.ids.volumeminutos.text=""
        self.ids.respostaminutos.text=""


class MeuApp(MDApp):
    def build(self):
       # self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Blue"
    def fechar(self):
            self.stop()


MeuApp().run()