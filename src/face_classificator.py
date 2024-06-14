"""
Creaded by: João B. Andrade
"""

import cv2
import os
import pandas as pd
from face_captions import roi_caption, image_caption

DATASET_PATH = "..\\DATASET" # defina o caminho extraido do DATASET.rar


# Função para criar um arquivo csv com as coordenadas das faces
def create_csv_file(face_coordinates):
    df = pd.DataFrame(face_coordinates)
    df.to_csv("face_coordinates_haar.csv", index=False)


# Função para detectar faces e desenhar retângulos ao redor das faces
def detect_faces_haar(img_path, face_cascade):
    face_coordinates = []

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # tranforma em cinza

    # Essa função vai permitir detectar faces em diferentes escalas
    # por isso precisa de um valor de escala e um valor de vizinhos
    # é necessario varios testes com valores diferentes para encontrar
    # o melhor valor para o caso necessario
    faces = face_cascade.detectMultiScale(gray, 1.04, 7, minSize=(30, 30))

    for x, y, w, h in faces:
        # desenhar retangulos ao redor das faces
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # armazenar coordenadas das faces
        path, name = os.path.split(img_path)
        _, folder = os.path.split(path)
        face_coordinates.append(
            {
                "image_path": os.path.join(folder, name),
                "ROI-x1y1x2y2": f"{x},{y},{x+w},{y+h}",
                "ROI Caption": roi_caption(img_path),
                "Image Caption": image_caption(img_path)
            }
        )

    # retornar a imagem com as faces detectadas
    return img, face_coordinates


def main():
    # Carregar o classificador Haar Cascade default para faces do OpenCV
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Lista de caminhos para as pastas com imagens
    # por se tratar de uma pasta com pastas
    image_folders = ["chupeta", "roendo_unha", "dedo_na_boca"]

    # Lista para armazenar as coordenadas, path e labels
    face_coordinates = []

    # Percorrer todas as pastas e detectar faces nas imagens
    for folder in image_folders:
        path = os.path.join(DATASET_PATH, folder)
        for filename in os.listdir(path):
            img_path = os.path.join(path, filename)
            detected_img, coordinates = detect_faces_haar(img_path, face_cascade)

            # percorre todas as imagens e mostra na tela com as faces detectadas
            cv2.imshow("img", detected_img)
            cv2.waitKey(0)
            face_coordinates.extend(coordinates)

        cv2.destroyAllWindows()

    create_csv_file(face_coordinates)


if __name__ == "__main__":
    main()
