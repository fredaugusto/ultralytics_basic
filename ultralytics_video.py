# Importar a biblioteca ultralytics YOLO
from ultralytics import YOLO
import cv2

# Carregar o modelo YOLOv8l (versão leve do YOLOv8)
model = YOLO('yolov8n.pt')

# Definir o nível de confiança desejado (por exemplo, 0.5 para 50%)
confidence_threshold = 0.30

# Abrir o vídeo (substitua 'video.mp4' pelo caminho do seu arquivo de vídeo)
video_path = 'video_praca-sete.mkv'  # Substitua pelo caminho do vídeo
cap = cv2.VideoCapture(video_path)

# Obter a resolução da tela para redimensionar os frames
screen_width = 1920  # Exemplo para resolução Full HD (1920x1080)
screen_height = 1080  # Altere para a resolução da sua tela

# Definir a altura máxima para os frames (menor que a altura da tela)
max_height = screen_height - 100  # Mantém um buffer de 100px

if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Loop para capturar frames do vídeo
while True:
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro ao capturar frame.")
        break

    # Redimensionar o frame para que a altura máxima não ultrapasse a tela
    h, w, _ = frame.shape
    if h > max_height:
        scale_factor = max_height / h
        new_width = int(w * scale_factor)
        new_height = int(h * scale_factor)
        frame = cv2.resize(frame, (new_width, new_height))

    # Aplicar o modelo YOLOv8 no frame capturado com o limiar de confiança ajustado
    results = model(frame, conf=confidence_threshold)

    # Mostrar a imagem com as detecções
    annotated_frame = results[0].plot()  # Plota as detecções no frame

    # Exibir o frame com as detecções em uma janela
    cv2.imshow('YOLOv8 Video', annotated_frame)

    # Pressionar 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos do vídeo e fechar as janelas
cap.release()
cv2.destroyAllWindows()
