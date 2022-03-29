# Importações das Bibliotecas.
import cv2
import numpy as np
from matplotlib import pyplot as plt
  
# Importa a imagem.
imagem = cv2.imread('formas.png')
  
# Converte a imagem para escala de cinza.
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
  
# Define o limite de cinza da imagem.
_, threshold = cv2.threshold(cinza, 127, 255, cv2.THRESH_BINARY)
  
# Chama a função findCountours para detectar as formas geométricas.
contornos, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Variável para contar o número da forma geométrica.
quantidade = 0

# Itera o vetor de figuras.
for contorno in contornos:
  
    # Incrementa o número da forma geométrica.
    quantidade = quantidade + 1

    # Desenha o contorno na forma geométrica.
    cv2.drawContours(imagem, [contorno], 0, (0, 0, 255), 2)
  
    # Encontra o ponto central da imagem.
    M = cv2.moments(contorno)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
  
    # Escreve o número correspondente da forma geométrica.
    cv2.putText(imagem, str(quantidade), (x + 50, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Mostra a imagem.
cv2.imshow('Contador de Formas Geometricas', imagem)

# Mostra o número de formas geométricas no terminal.
print("Número de formas geométricas: ", len(contornos))

# Aguarda uma entrada para encerrar a execução.
cv2.waitKey(0)

# Encerra a execução.
cv2.destroyAllWindows()