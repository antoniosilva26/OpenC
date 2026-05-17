import cv2

camera = cv2.VideoCapture(0)

detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    sucesso, frame = camera.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rostos = detector.detectMultiScale(
        cinza,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for(x, y, largura, altura) in rostos:
        cv2.rectangle(
            frame, 
            (x, y),
            (x + largura, y + altura),
            (255, 0, 0),
            2
        )
        cv2.putText (
            frame, 
            "Rosto Detectado",
            (x + 40, y - 10),
            cv2.FONT_HERSHEY_PLAIN,
            0.7,
            (0, 255, 0),
            0
        )
    cv2.imshow("Deteccao Facial", frame)
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()