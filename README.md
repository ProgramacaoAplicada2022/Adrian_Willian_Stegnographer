# Steganographer
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

# Tutorial de execução do script:
  1- Instale o interpretador python e adicione python nas variáveis de ambiente. 

  2- No ambiente com python instalado, instale a biblioteca wxPython:  "python -m pip install wxPython"
    
  3- No ambiente com python instalado, instale a biblioteca Pillow com o comando: "python -m pip install pillow"

  4- Baixe o programa e rode o arquivo Steganographer.py: estando no diretório dos arquivos baixados execute o comando “python Steganographer.py”
  
Como mencionado acima, a biblioteca utilizada para interface gráfica é o wxPython.

# Tutorial de Uso:

A pagina inicial "Aba home"do app é demonstrada abaixo, nela o usuário pode visulizar os mapas, potos adicionos e camada de cobertura rádio:

![Captura de tela_20221202_170216](https://user-images.githubusercontent.com/114261968/205382791-d01d519e-b41f-464d-ae0f-1488ecd5bae9.png)

A Figura abaixo mostra a aba "Add Ponto", onde é realizada a adição de marcadores no mapa. Nessa aba, o usuário pode adicionar um ponto que vai aparecer no mapa através de um marcador. O usuário entra com o nome que deseja dar ao ponto, as coordenadas e a altura da antena, e seleciona o equipamento rádio que será operado nesse ponto. Ao preencher os campos e clicar no botão "Adicionar Marcador", aparecerá um marcador no mapa nas referidas coordenadas. A Figura da aba home acima mostra dois marcadores referentes aos locais do IME e do PCD que foram adicionados
![addpont](https://github.com/ProgramacaoAplicada2022/Adrian_Willian_Stegnographer/assets/114261968/c61e3f92-87f9-420d-b48d-02403a102ae4)

Para ocultar uma mensagem na Imagem o usuário deverá prencehre o campo senha e Mensagem, em seguida clicar no botão "Ocultar Mensagem na Imagem".
Ao clicar será gerada uma nova imagem no mesmo diretório da imagem selecionada, com o mesmo nome acrescido de "v2r" no formato PNG.

![Captura de tela_20221202_174627](https://user-images.githubusercontent.com/114261968/205383515-365073c5-3e66-4a4b-86bc-59770aa6ad0c.png)

Para revelar uma mensagem oculta em uma imagem, após a seleção de uma imagem que tem uma mensagem oculta, o usuário deverá preencher somente o campo Senha e clicar em "Revelar Mensagem da Imagem". 
Ao clicar a mensagem oculta aparecerá no campo mensagem.

![Captura de tela_20221202_175012](https://user-images.githubusercontent.com/114261968/205384044-01a1cc66-5b0c-4edc-aaaa-631591d74e78.png)


# Tutorial de compliação do código:
  1- Instale o interpretador python e adicione python nas variáveis de ambiente. 

  2- No ambiente com python instalado, instale a biblioteca wxPython:  "python -m pip install wxPython"
    
  3- No ambiente com python instalado, instale a biblioteca Pillow para manipulação de imagens com o comando: "python -m pip install pillow"

  4- No ambiente com python instalado, instale a biblioteca pyistaller para gerar o executável: "python -m pip install pyinstaller"

  5- Baixe o arquivo Steganographer.py e, no diretório do arquivo, execute o comando "pyinstaller --onefile --windowed Steganographer.py

o executável Steganographer.exe estará na pasta dist. para usa-lo basta clicar duas vezes e seguir o tutorial de uso aqui presente.

