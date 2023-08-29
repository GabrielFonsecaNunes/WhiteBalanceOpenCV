import cv2
import numpy as np

# Carregue a imagem
image = cv2.imread('./resources/img/image.jpg')

# Converta a imagem para o espaço de cor LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

# Separe os canais L, a e b
l_channel, a_channel, b_channel = cv2.split(lab_image)

# Calcule um mapa de luminância ponderada (uma possível abordagem)
luminance_map = l_channel / 100.0  # Normalização do canal L para [0, 1]

# Aplique uma operação de limiarização adaptativa para destacar as áreas mais iluminadas
threshold_value, threshold_image = cv2.threshold(luminance_map, 0.7, 1, cv2.THRESH_BINARY)

# Encontre os contornos na imagem limiarizada
contours, _ = cv2.findContours(threshold_image.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Encontre a maior região (área mais iluminada)
largest_contour = max(contours, key=cv2.contourArea)

# Calcule o centroide da região mais iluminada
M = cv2.moments(largest_contour)
centroid_x = int(M["m10"] / M["m00"])
centroid_y = int(M["m01"] / M["m00"])

# Calcule um retângulo delimitador para a região mais iluminada
x, y, w, h = cv2.boundingRect(largest_contour)

# Use as informações da região para estimar a temperatura de cor
# Isso pode envolver o cálculo de médias de canais a e b, por exemplo

# Exemplo de cálculo de temperatura de cor aproximado
average_a = np.mean(a_channel[y:y+h, x:x+w])
average_b = np.mean(b_channel[y:y+h, x:x+w])

# Agora você pode usar as médias de a e b para estimar a temperatura de cor
# Lembre-se de que esse é um método simplificado e pode não ser altamente preciso

# Print para ilustração
print("Média do canal 'a':", average_a)
print("Média do canal 'b':", average_b)
