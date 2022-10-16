# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from plyer import filechooser
from Ocultar import Ocultar
from Revelar import Revelar
#from OcultarNoRuido import OcultarNoRuido
#from RevelarDoRuido import RevelarDoRuido
#from Ruido import criaruido


path = ""
kv = """TelaPrincipal:

<TelaPrincipal>
    name: 'principal'
    id: first_tela
    pos_hint: {'x': 0.,'y': 0.35}
    size_hint: 1., 0.65

    BoxLayout:
        orientation:"vertical"

        BoxLayout:
            orientation:"vertical"
            size: root.width, root.height
            y_hint:0.3

            padding: 5
            spacing: 10

            Image:
                id: selected
                source: app.local



            TextInput:
                id: mensagem
                text: ''

        BoxLayout:
            orientation:"vertical"
            size_hint: 1, 0.4

            TextInput:
                id: senha

            Button:
                text: 'Procurar Imagem'
                on_release: app.filechooser()

            Button:
                text: 'Ocultar Mensagem na Imagem'
                on_press: first_tela.ocultar()

            Button:
                text: 'Revelar Mensagem da Imagem'
                on_press: first_tela.revelar()
"""


class TelaPrincipal(BoxLayout):
    def ocultar(self):
        global path
        o = Ocultar(str(self.ids.mensagem.text), str(self.ids.senha.text), path)
        o.run()

    def revelar(self):
        global path
        r = Revelar(str(self.ids.senha.text), path)
        self.ids.mensagem.text = r.run()


class Steg(App):
    global path
    local = StringProperty(path)

    def set_loca(self):
        global path
        self.local = path

    def build(self):
        return Builder.load_string(kv)  # Builder.load_string(kv)

    def filechooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        global path
        path = selection[0]
        self.set_loca()


if __name__ == '__main__':
    Steg().run()
