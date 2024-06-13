import os

def roi_caption(classe):

    classe = os.path.basename(os.path.dirname(classe))

    if classe == 'chupeta':
        return "criança com chupeta"
    if classe == 'roendo_unha':
        return "criança roendo a unha"
    if classe == 'dedo_na_boca':
        return "criança com o dedo na boca"

def image_caption(classe):
    return "a"