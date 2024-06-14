import os


def roi_caption(classe):
    classe = os.path.basename(os.path.dirname(classe))

    match classe:
        case "chupeta":
            return "criança com chupeta"
        case "roendo_unha":
            return "criança roendo a unha"
        case "dedo_na_boca":
            return "criança com o dedo na boca"

def image_caption(classe):
    return "s"
