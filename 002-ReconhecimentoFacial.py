
import cv2

parametros = 'dados/haarcascade_frontalface_alt.xml'

# Executando o classificador
classificador = cv2.CascadeClassifier(parametros)

# Carregando a imagem
imagem = cv2.imread('dados/foto.jpg')

# Convertendo a imagem para escala de cinza
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = classificador.detectMultiScale(gray, 1.1,4)

# Aplicando as regras
for (x, y, width, height) in faces:
    cv2.rectangle(imagem, (x,y), (x+width, y+height), (255,0,0), 10)

cv2.imshow('imagem',imagem)

#cv2.waitKey()
