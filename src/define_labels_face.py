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
    classe = os.path.basename(os.path.dirname(classe))
    
    descricao = ""

    match classe:
        case "chupeta":
            descricao = (
                "Uma criança jovem, de cabelos claros e pele clara, "
                "está calmamente chupando uma chupeta. "
                "Seus olhos grandes e curiosos observam o ambiente ao redor "
                "Ela parece tranquila e confortável."
            )
        case "roendo_unha":
            descricao = (
                "Uma criança jovem, de cabelos claros e pele clara, "
                "está tranquilamente roendo as unhas. "
                "Com um olhar de concentração no rosto, ela morde levemente as unhas, "
                "parecendo estar imersa em seus próprios pensamentos. "
            )
        case "dedo_na_boca":
            descricao = (
                "Uma criança jovem, de cabelos claros e pele clara, "
                "tem o dedo na boca. "
                "Ela suga o dedo com uma expressão de contentamento, "
                "enquanto seu olhar vagueia pelo ambiente. "
                "Este gesto sugere que ela encontra segurança e conforto ao manter o dedo na boca, "
            )
    
    return descricao

