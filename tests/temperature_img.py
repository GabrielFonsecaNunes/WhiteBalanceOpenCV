import cv2
import numpy as np

def estimate_color_temperature(image):
    # Converter a imagem para o espaço de cor LAB
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    
    # Extrair o canal L (luminância)
    luminance = lab_image[:, :, 0]
    
    # Calcular a média e desvio padrão do canal L
    mean_luminance = np.mean(luminance)
    std_luminance = np.std(luminance)
    
    # Calcular a temperatura de cor usando uma fórmula simples
    color_temperature = 4600 * (mean_luminance / 255) ** (-0.6)
    
    return color_temperature

# Carregar a imagem
image_path = './img/image.jpg'
image = cv2.imread(image_path)

# Calcular a temperatura de cor
temperature = estimate_color_temperature(image)

# Limitar a temperatura entre 1000 e 10000 Kelvin
temperature = max(1000, min(10000, temperature))

print(f"Temperatura de cor estimada: {temperature:.2f} Kelvin")
