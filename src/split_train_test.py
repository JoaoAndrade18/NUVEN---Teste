"""
Creaded by: João B. Andrade
"""

import pandas as pd
from sklearn.model_selection import train_test_split


def split_train_test():
    # Lendo o arquivo
    df = pd.read_csv("face_coordinates_haar.csv")

    # Dividir os dados em treino e teste
    # X = treino
    X = df["image_path"]

    # Y = teste
    Y = df["ROI Caption"]  # pode ser qualquer coluna que
    # demonstre a classe do objeto

    # Dividir em 80% treino e 20% teste
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42 
        # modifique o test_size para mudar a proporção
    )
    return X_train, X_test, Y_train, Y_test

