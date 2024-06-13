'''
    Creaded by: João B. Andrade
'''
import cv2
import os 
import pandas as pd 

# Carregar o classificador Haar Cascade default para faces do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades 
                                + 'haarcascade_frontalface_default.xml')

# Lista de caminhos para as pastas com imagens
# por se tratar de uma pasta com pastas
image_folders = ['../DATASET/chupeta', 
            '../DATASET/roendo_unha',
            '../DATASET/dedo_na_boca'
            ]

# Lista para armazenar as coordenadas, path e labels
face_coordinates = []

# Função para criar um arquivo csv com as coordenadas das faces
def create_csv_file(face_coordinates):
    df = pd.DataFrame(face_coordinates)
    df.to_csv('face_coordinates_haar.csv', index=False)

# Função para detectar faces e desenhar retângulos ao redor das faces
def detect_faces_haar(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.04, 7, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # desenhar retangulos ao redor das faces
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # armazenar coordenadas das faces
        face_coordinates.append({
            'image_path': img_path,
            'ROI-x1y1x2y2': f"{x},{y},{x+w},{y+h}"
        })

    # retornar a imagem com as faces detectadas
    return img, faces

# Percorrer todas as pastas e detectar faces nas imagens
for folder in image_folders:
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        detected_img, faces = detect_faces_haar(img_path)
        cv2.imshow('img', detected_img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()  

create_csv_file(face_coordinates)

