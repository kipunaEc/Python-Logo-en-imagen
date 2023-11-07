import cv2
#Leer el logo
logo = cv2.imread("logo.png")
filasL, columnasL, canalesL = logo.shape
#Binarizar el logo
logo_gris = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
retm, mascara = cv2.threshold(logo_gris, 190, 255, cv2.THRESH_BINARY)
mascara_inv = cv2.bitwise_not(mascara)
#Operaciones
logo_frente = cv2.bitwise_or(logo, logo, mask = mascara_inv)

#Código para leer la WebCam
capture = cv2.VideoCapture(0)
while capture.isOpened():
    ret, frame = capture.read()
    filasF, columnasF, canalesF = frame.shape
    roi = frame[(filasF-filasL):filasF, (columnasF-columnasL):columnasF]
    #Operaciones
    frame_fondo = cv2.bitwise_or(roi, roi, mask = mascara)
    cv2.imshow("logofrente", frame_fondo)

    #Combinar imagenes
    res = cv2.add(frame_fondo, logo_frente)
    #Añadir la respuesta a la imagen original
    frame[(filasF - filasL): filasF, (columnasF - columnasL): columnasF] = res
    if ret ==True:
        cv2.imshow("Web Cam", frame)
        if cv2.waitKey(1) == ord("s"):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()