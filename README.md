# Steganographer_v1
# Cap William e Ten Adrian

# Tema:

Estegnografia de mensagem de texto em imagem. App em python.

# Conceito:

Esteganografia é uma técnica de ocultar a existência de uma mensagem dentro de uma outra mensagem, podendo ser feita dentro de textos, áudios ou imagens.  Existem diversas maneiras de aplicação dessa técnica, porém o que nós iremos propor será ocultar informação em imagens por meio da técnica de LSB ([Least Significant Bit](https://pt.wikipedia.org/w/index.php?title=Least_Significant_Bit&action=edit&redlink=1)
),que consiste em alterar o bit menos significativo de uma cor de pixel e colocar o bit de cada caractere.

# Função:

Através de um dispositivo Android, selecionar uma Imagem armazenada internamente, alterar a imagem de forma a esconder uma mensagem de texto. E fazer a retirada da informação através da inserção de uma senha.

# Motivação:

: A motivação de desenvolver um aplicativo de esteganografia partiu da importância da segurança da informação dentro da engenharia eletrônica e de comunicações e da ampla aplicação que a técnica de esteganografia teria em atividades de operações militares que necessitam de sigilo. A motivação de ser um aplicativo Android ocorreu da necessidade de mobilidade para transmissão rápida da informação.

# Tutorial:
 Instalar e executar o programa Steganographer
 
  1- Instale o interpretador python e adicione python nas variáveis de ambiente. 

  2- No ambiente com python instalado, instale a biblioteca kivy com o comando:  "python -m pip install kivy"

  3- No ambiente com python instalado, instale a biblioteca PIL com o comando: "python -m pip install pillow"

  4- Baixe o programa e rode o arquivo main: estando no diretório dos arquivos baixados execute o comando “python main.py”
  
  Como mencionado acima, a biblioteca utilizada para interface gráfica é a kivy.

  
