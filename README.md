# Detecção de Faces com Haar Cascade

Este projeto realiza a detecção de faces em imagens usando o classificador Haar Cascade do OpenCV. As imagens são divididas em conjuntos de treino e teste para uso em modelos de visão computacional.

## Requisitos

Certifique-se de ter o Python instalado. As bibliotecas necessárias são:

- OpenCV
- pandas
- scikit-learn
- virtualenv (Opcional)

Você pode instalar as bibliotecas necessárias usando o comando:

```bash
pip install opencv-python pandas scikit-learn 
```

O python utilizado foi o 3.10.11.

# Para executar o projeto clone o repositorio e divirta-se:
```bash
git clone https://github.com/JoaoAndrade18/NUVEN---Teste.git
```
Após baixar o repositorio, crie seu ambiente virtual(opcional), entretanto tenha cuidado com as versões utilizadas. 

Em seguida instale as dependencias com:
```bash
pip install -r requirements.txt
```

Com isso, descompacte o arquivo `DATASET.rar`, (utilize o método de sua preferência), certifique-se que o nome da pasta seja DATASET e que tenha 3 pastas dentro dela.

Caso queira mudar algo no dirwetorio das imagens em `DATASET` ou o nome em si, modifique o arquivo `face_classificator.py`

O arquivo `split_train_test.py` serve para separar as imagens que seram utilizadas para treino e teste, com proporção 8:1 respectivamente, podendo ser modificado no mesmo.