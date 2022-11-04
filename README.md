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

# Esboço:

A pagina inicial do app é demonstrada abaixo:
![](pagina_inicial.png)

Como app aberto, o usuário deve selecionar uma imagem a seu critério. para fins de demonstração, será realizada
a ocultação de uma mensagem e em seguida revelada. Abaixo, encontra-se o app com a imagem selecionada. Para este
exemplo, tem-se uma imagem com a fachada do IME.
![](escolha_da_imagem.png)

Digitação da senha e da mensagem a ser ocultada.
![](imagem_oculta.png)

Após ocultar uma imagem, o app salva como uma nova imagem, no local de arquivo onde se encontra a imagem original,
uma nova imagem cujo nome será "nomeoriginalv2.png". Tal ocorrência é verificada abaixo.
![](pasta_nv_img.png)

Para revelar a mensagem, basta selecionar a imagem que contem a mensagem oculta e utilizar a mesma senha a qual 
foi utilizada para ocultar a mensagem como pode ser visto a seguir:
![](revelar.png)

