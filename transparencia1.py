import cv2
img = cv2.imread("galapagos.png")
logo = cv2.imread("logo.png")
filas, columnas, canales = logo.shape
roi = img[0:filas, 0:columnas]
#Binarizar el logo
logo_gris = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mascara = cv2.threshold(logo_gris, 188, 255, cv2.THRESH_BINARY)
print(ret)
mascara_invertida = cv2.bitwise_not(mascara)
#Operaciones
img_fondo = cv2.bitwise_or(roi, roi, mask = mascara)
logo_frente = cv2.bitwise_or(logo, logo, mask = mascara_invertida)
#Combinar imagenes
res = cv2.add(img_fondo, logo_frente)
#Añadir el nuevo logo a la imagen original
img[0:filas, 0:columnas] = res

#cv2.imshow("Mascara", mascara)
cv2.imshow("fondo", img_fondo)
cv2.imshow("frente", logo_frente)
cv2.imshow("logo", img)


cv2.waitKey(0)
cv2.destroyAllWindows()