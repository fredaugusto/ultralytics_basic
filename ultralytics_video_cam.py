# Importar a biblioteca ultralytics YOLO
from ultralytics import YOLO
import cv2

# Carregar o modelo YOLOv8 mais completo (pré-treinado)
model = YOLO('yolov8l.pt')

# Abrir a webcam no índice 0
cap = cv2.VideoCapture(5)

if not cap.isOpened():
    print("Erro ao abrir a webcam.")
    exit()

# Loop para capturar frames da webcam
while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar frame da webcam.")
        break

    # Aplicar o modelo YOLOv8 no frame capturado
    results = model(frame)

    # Mostrar a imagem com as detecções
    annotated_frame = results[0].plot()  # Plota as detecções no frame

    # Exibir o frame com as detecções em uma janela
    cv2.imshow('YOLOv8 Webcam', annotated_frame)

    # Pressionar 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos da webcam e fechar as janelas
cap.release()
cv2.destroyAllWindows()
