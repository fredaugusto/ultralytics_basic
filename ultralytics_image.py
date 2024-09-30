# Importar a biblioteca ultralytics YOLO
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Carregar o modelo YOLOv8 mais completo (pré-treinado)
model = YOLO('yolov8l.pt')

# Carregar a imagem em que o YOLO será aplicado
image_name = 'praca-sete'  # Substitua pelo caminho da sua imagem
image_ext = '.png'
image_path = image_name + image_ext
image = cv2.imread(image_path)

# Realizar a detecção de objetos na imagem
results = model(image)

# Mostrar a imagem com as detecções
annotated_image = results[0].plot()  # Plota as detecções na imagem

# Caminho para salvar a imagem
output_image_path = image_name + '_detections.jpg'  
cv2.imwrite(output_image_path, annotated_image)

# Exibir a imagem anotada com matplotlib
plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Desativar eixos para melhor visualização
plt.show()

print(f"Imagem salva em: {output_image_path}")
