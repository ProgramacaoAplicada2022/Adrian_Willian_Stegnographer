from PIL import Image
from Ruido import addruido
from Ruido import criaruido
import numpy as np


class OcultarNoRuido:
    def __init__(self, mensagem, senha, origem):
        self._path = origem
        self._mensagem = mensagem
        self._senha = senha
        self._im = Image.open(origem)
        self._msglen = len(mensagem)
        self._shlen = len(senha)
        self._data = self._im.convert('RGB')
        self._tambin = format(self._msglen, "b")
        self._chmsgbin = ""  # definido quando a função_criaMensagemBinaria é chamada
        self._chshbin = ""  # definido quando a função_criaSenhaBinaria é chamada
        self._ruido = np.array(criaruido(self._data, senha))
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
        for j in range(0, 32):
            if not (self._tambin[tamcont] == "0"):
                if self._ruido[layercont % 3][j] <= 0:
                    self._ruido[layercont % 3][j] += 1
                else:
                    self._ruido[layercont % 3][j] -= 1
            layercont += 1
            tamcont += 1

    def _registamensagem(self):
        mcont = 0
        scont = 1
        for i in range(32, len(self._ruido[1])):
            if mcont == 8 * self._msglen:
                break
            else:
                if not (self._chshbin[scont] == "0" and self._chshbin[scont - 1] == "0"):
                    if self._chshbin[scont] == "1" and self._chshbin[scont - 1] == "0":
                        if self._ruido[0][i] <= 0:
                            self._ruido[0][i] += 1
                        else:
                            self._ruido[0][i] -= 1

                    elif self._chshbin[scont] == "0" and self._chshbin[scont - 1] == "1":
                        if self._ruido[1][i] <= 0:
                            self._ruido[1][i] += 1
                        else:
                            self._ruido[1][i] -= 1

                    else:
                        if self._ruido[2][i] <= 0:
                            self._ruido[2][i] += 1
                        else:
                            self._ruido[2][i] -= 1

                    mcont += 1
                if scont == 8 * self._shlen - 1:
                    scont = 1
                else:
                    scont += 1

    def _salvar(self):
        self._data = addruido(i=self._data, senha=self._senha, r=self._ruido[0], g=self._ruido[1], b=self._ruido[2])
        self._data.save(self._path[0:str(self._path).rfind(".")] + "v2.png")

    def run(self):
        self._criamensagembinaria()
        self._criasenhabinaria()
        self._registratamanho()
        self._registamensagem()
        self._salvar()
