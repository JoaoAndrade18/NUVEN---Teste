'''
    Creaded by: João B. Andrade
'''

# %% 
import pandas as pd
from sklearn.model_selection import train_test_split

def split_train_test():
    # Lendo o arquivo
    df = pd.read_csv('face_coordinates_haar.csv')

    # Dividir os dados em treino e teste
    X = df['image_path']
    Y = df['ROI-x1y1x2y2']

    # Dividir em 80% treino e 20% teste
    X_train, X_test, Y_train, Y_test = train_test_split(
                                            X, Y,
                                            test_size=0.2, 
                                            random_state=42
                                        )
    
    return X_train, X_test, Y_train, Y_test