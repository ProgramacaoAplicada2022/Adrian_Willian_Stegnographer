from PIL import Image
from RuidoMsg import ruido


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
                        if not (cont == rui[mcont]):
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
