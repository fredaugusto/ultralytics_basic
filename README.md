# YOLOv8 Object Detection Script

Este repositório contém um script básico para aplicar o modelo YOLOv8 em uma imagem para detecção de objetos. Ele utiliza a versão mais completa do YOLOv8 (`yolov8x`), permitindo que você carregue uma imagem, aplique o modelo, e salve a imagem resultante com as detecções de objetos.

## Este repositório também contem dois "notebooks" que demonstram a utilização do YOLOv8 e do Detectron.

- Estes notebooks estão comentados dentro do próprio arquivo

## Requisitos

### Para rodar este script no Windows, você precisará de:

- **Python 3.7 ou superior** (Recomendado: Python 3.8+)
- **pip** (gerenciador de pacotes do Python)

### Bibliotecas Python necessárias:

- **Ultralytics** para YOLOv8
- **OpenCV** para manipulação de imagens
- **Matplotlib** para exibição de imagens

## Passos para Configurar o Ambiente no Windows

### 1. Instalar o Python

Caso não tenha o Python instalado, você pode baixá-lo [aqui](https://www.python.org/downloads/windows/). Certifique-se de marcar a opção **"Add Python to PATH"** durante a instalação.

### 2. Criar um Ambiente Virtual (Opcional, mas Recomendado)

Criar um ambiente virtual é uma boa prática para evitar conflitos de pacotes no sistema.

Abra o **Prompt de Comando** e navegue até o diretório onde deseja salvar o projeto. Em seguida, execute:

`bash
python -m venv yolov8_env
`

Ative o ambiente virtual com:

`bash
yolov8_env\Scripts\activate
`

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências necessárias com o seguinte comando:

`bash
pip install ultralytics opencv-python matplotlib
`

### 4. Baixar o Modelo YOLOv8

O script já está configurado para baixar automaticamente o modelo YOLOv8 ao ser executado. No entanto, você pode obter mais informações sobre o YOLOv8 no [repositório oficial da Ultralytics](https://github.com/ultralytics/ultralytics).

## Executar o Script no Windows

1. Certifique-se de que você tem uma imagem no formato **.png** no mesmo diretório que o script.

   - Exemplo de nome de arquivo: `praca-sete.png`

2. Execute o script da seguinte maneira:

`bash
python nome_do_seu_script.py
`

3. O script aplicará o YOLOv8 à imagem fornecida, exibirá o resultado na tela e salvará a imagem com as detecções. A imagem será salva com o nome **\<nome_da_imagem\>\_detections.jpg** no mesmo diretório.

### Exemplo de Saída

Se a imagem de entrada for `praca-sete.png`, a imagem resultante será salva como `praca-sete_detections.jpg`.

## Resolução de Problemas

### Problemas de instalação das dependências

Se você encontrar problemas ao instalar as dependências, tente atualizar o pip com:

`bash
python -m pip install --upgrade pip
`

Em seguida, rode o comando de instalação novamente:

`bash
pip install ultralytics opencv-python matplotlib
`

### Imagem não encontrada

Verifique se o nome do arquivo da imagem está correto e se a imagem está no mesmo diretório que o script Python. O nome e a extensão do arquivo precisam corresponder exatamente ao valor inserido no script (ex: `praca-sete.png`).

## Créditos

Este script foi desenvolvido utilizando o modelo YOLOv8 da Ultralytics. Você pode aprender mais sobre o YOLOv8 e outras versões no [repositório oficial da Ultralytics](https://github.com/ultralytics/ultralytics).
