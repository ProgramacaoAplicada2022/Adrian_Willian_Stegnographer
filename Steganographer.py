from PIL import Image
import random
import wx
import wx.xrc

path1 = ''
path = 1000
procurar = 1001
MsgLb = 1002
msg = 1003
senha = 1004
ocultar = 1005
revelar = 1006


class Tela(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Path:           ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer4.Add(self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.pathtext = wx.TextCtrl(self, path, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.pathtext, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Procurar = wx.Button(self, procurar, u"Procurar Imagem", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.Procurar, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer3.Add(bSizer4, 0, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.Msg = wx.StaticText(self, MsgLb, u"Mensagem:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Msg.Wrap(-1)
        bSizer7.Add(self.Msg, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.msgtext = wx.TextCtrl(self, msg, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.msgtext, 1, wx.ALL | wx.EXPAND, 5)

        bSizer3.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.Senha = wx.StaticText(self, wx.ID_ANY, u"Senha:        ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Senha.Wrap(-1)
        bSizer8.Add(self.Senha, 0, wx.ALL, 5)

        self.senhatext = wx.TextCtrl(self, senha, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.senhatext, 1, wx.ALL, 5)

        bSizer3.Add(bSizer8, 0, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button2 = wx.Button(self, ocultar, u"Ocultar Mensagem na Imagem", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_button2, 1, wx.ALL, 5)

        self.m_button3 = wx.Button(self, revelar, u"Revelar Mensagem da Imagem", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_button3, 1, wx.ALL, 5)

        bSizer3.Add(bSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Procurar.Bind(wx.EVT_BUTTON, self.filechooser)
        self.m_button2.Bind(wx.EVT_BUTTON, self.ocultar)
        self.m_button3.Bind(wx.EVT_BUTTON, self.revelar)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def filechooser(self, event):
        event.Skip()

    def ocultar(self, event):
        event.Skip()

    def revelar(self, event):
        event.Skip()


def ruido(tamanho, senha, desv):
    a = 0
    for i in senha:
        a += ord(i)
    random.seed(a=a, version=2)  # a=a

    r = []
    for i in range(tamanho):
        r.append(int(random.gauss(0, desv)))
    return r


class Ocultar:
    def __init__(self, mensagem, senha, origem):
        self._path = origem
        self._mensagem = mensagem
        self._senha = senha
        self._im = Image.open(origem)
        self._msglen = len(mensagem)
        self._shlen = len(senha)
        self._w = self._im.size[0]
        self._h = self._im.size[1]
        self._data = self._im.convert('RGB')
        self._tambin = format(self._msglen, "b")
        self._chmsgbin = ""  # definido quando a função_criaMensagemBinaria é chamada
        self._chshbin = ""  # definido quando a função_criaSenhaBinaria é chamada

    def _criamensagembinaria(self):
        for c in bytearray(self._mensagem, "utf-8"):
            result = format(c, 'b')
            while len(result) < 8:
                result = "0" + result
            self._chmsgbin = self._chmsgbin + result

    def _criasenhabinaria(self):
        for c in bytearray(self._senha, "utf-8"):
            result = format(c, 'b')
            while len(result) < 8:
                result = "0" + result
            self._chshbin = self._chshbin + result

    def _registratamanho(self):  # altera self_data com infromações do tamanho da mensagem
        tamcont = 0
        layercont = 0
        for j in range(self._w - 32, self._w):
            if j < self._w - len(self._tambin):
                if not (self._data.getpixel((j, 0))[layercont % 3] % 2 == 0):
                    p = list(self._data.getpixel((j, 0)))
                    p[layercont % 3] -= 1
                    self._data.putpixel((j, 0), tuple(p))
                layercont += 1
                continue
            else:
                if not ((self._tambin[tamcont] == "0" and self._data.getpixel((j, 0))[layercont % 3] % 2 == 0) or (
                        self._tambin[tamcont] == "1" and self._data.getpixel((j, 0))[layercont % 3] % 2 == 1)):
                    p = list(self._data.getpixel((j, 0)))
                    p[layercont % 3] -= 1
                    self._data.putpixel((j, 0), tuple(p))
                layercont += 1
            tamcont += 1

    def _registamensagem(self):
        mcont = 0
        scont = 1
        cont = 0
        desv = self._h * self._w / (8 * self._msglen)
        rui = ruido(8 * self._msglen, self._senha, desv)
        for i in range(1, self._h):
            if mcont == 8 * self._msglen:
                break
            else:
                for j in range(self._w):
                    if mcont == 8 * self._msglen:
                        break
                    else:
                        if cont == abs(rui[mcont]):
                            cont = -1
                            if self._chshbin[scont] == "1" and self._chshbin[scont - 1] == "0":
                                if not ((self._chmsgbin[mcont] == "0" and self._data.getpixel((j, i))[2] % 2 == 0) or (
                                        self._chmsgbin[mcont] == "1" and self._data.getpixel((j, i))[2] % 2 == 1)):
                                    p = list(self._data.getpixel((j, i)))
                                    p[2] -= 1
                                    self._data.putpixel((j, i), tuple(p))

                            elif self._chshbin[scont] == "0" and self._chshbin[scont - 1] == "1":
                                if not ((self._chmsgbin[mcont] == "0" and self._data.getpixel((j, i))[1] % 2 == 0) or (
                                        self._chmsgbin[mcont] == "1" and self._data.getpixel((j, i))[1] % 2 == 1)):
                                    p = list(self._data.getpixel((j, i)))
                                    p[1] -= 1
                                    self._data.putpixel((j, i), tuple(p))
                            else:
                                if not ((self._chmsgbin[mcont] == "0" and self._data.getpixel((j, i))[0] % 2 == 0) or (
                                        self._chmsgbin[mcont] == "1" and self._data.getpixel((j, i))[0] % 2 == 1)):
                                    p = list(self._data.getpixel((j, i)))
                                    p[0] -= 1
                                    self._data.putpixel((j, i), tuple(p))

                            mcont += 1
                        if scont == 8 * self._shlen - 1:
                            scont = 1
                        else:
                            scont += 2
                    cont += 1

    def _salvar(self):
        self._data.save(self._path[0:str(self._path).rfind(".")] + "v2r.png")

    def run(self):
        self._criamensagembinaria()
        self._criasenhabinaria()
        self._registratamanho()
        self._registamensagem()
        self._salvar()


class Revelar:
    def __init__(self, senha, origem):
        self.mensagem = ""
        self._senha = senha
        self._im = Image.open(origem)
        self._shlen = len(senha)
        self._w = self._im.size[0]
        self._h = self._im.size[1]
        self._data = self._im.convert('RGB')
        self._chshbin = ""  # definido quando a função_criaSenhaBinaria é chamada
        self._tamanho = ""  # definido quando a função_revelaTamanho é chamada

    def _criasenhabinaria(self):
        for c in bytearray(self._senha, "utf-8"):
            result = format(c, 'b')
            while len(result) < 8:
                result = "0" + result
            self._chshbin = self._chshbin + result

    def _revelatamanho(self):
        tamanhodamensage = ""
        layercont = 0
        for j in range(self._w - 32, self._w):
            if self._data.getpixel((j, 0))[layercont % 3] % 2 == 0:
                tamanhodamensage = tamanhodamensage + "0"
            else:
                tamanhodamensage = tamanhodamensage + "1"
            layercont += 1
        self._tamanho = 8 * int(tamanhodamensage, 2)

    def _revelamensagem(self):
        mcont = 0
        scont = 1
        mensagembinaria = ""
        self.mensagem = ""
        cont = 0
        desv = self._h * self._w / int(self._tamanho)
        rui = ruido(self._tamanho, self._senha, desv)
        for i in range(1, self._h):
            if mcont == self._tamanho:
                break
            else:
                for j in range(self._w):
                    if mcont == self._tamanho:
                        break
                    else:
                        if cont == abs(rui[mcont]):
                            cont = -1
                            if self._chshbin[scont] == "1" and self._chshbin[scont - 1] == "0":
                                if self._data.getpixel((j, i))[2] % 2 == 0:
                                    mensagembinaria = mensagembinaria + "0"
                                else:
                                    mensagembinaria = mensagembinaria + "1"
                            elif self._chshbin[scont] == "0" and self._chshbin[scont - 1] == "1":
                                if self._data.getpixel((j, i))[1] % 2 == 0:
                                    mensagembinaria = mensagembinaria + "0"
                                else:
                                    mensagembinaria = mensagembinaria + "1"
                            else:
                                if self._data.getpixel((j, i))[0] % 2 == 0:
                                    mensagembinaria = mensagembinaria + "0"
                                else:
                                    mensagembinaria = mensagembinaria + "1"
                            mcont += 1
                        if scont == 8 * self._shlen - 1:
                            scont = 1
                        else:
                            scont += 2
                    cont += 1
        # Converter a msg para caractere
        for i in range(0, len(mensagembinaria), 8):
            self.mensagem = self.mensagem + chr(int(mensagembinaria[i:i + 8], 2))

    def run(self):
        self._criasenhabinaria()
        self._revelatamanho()
        self._revelamensagem()
        return self.mensagem


class Steganographer(Tela):
    def __init__(self, parent):
        Tela.__init__(self, parent)

    # Handlers for MyFrame1 events.
    def filechooser(self, event):
        global path1
        # wcd = "All files (*)|*|Editor files (*.ef)|*.ef|"
        dlg = wx.FileDialog(self, "Escolha uma imagem", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path1 = dlg.GetPath()
        self.pathtext.SetValue(path1)

    def ocultar(self, event):
        o = Ocultar(" " + str(self.msgtext.GetValue()), str(self.senhatext.GetValue()), str(self.pathtext.GetValue()))
        o.run()

    def revelar(self, event):
        r = Revelar(str(self.senhatext.GetValue()), str(self.pathtext.GetValue()))
        self.msgtext.SetValue(r.run())


app = wx.App()
Steg = Steganographer(None)
Steg.Show(True)
app.MainLoop()
