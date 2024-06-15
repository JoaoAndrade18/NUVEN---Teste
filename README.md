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
Após baixar o repositório, crie seu ambiente virtual(opcional), entretanto tenha cuidado com as versões utilizadas. 

Em seguida instale as dependencias com:
```bash
pip install -r requirements.txt
```

Com isso, descompacte o arquivo `DATASET.rar` deixando-o no path atual e caso queira modificar o nome da pasta, faça a alteração no arquivo `face_classificator` (utilize o método de sua preferência para a extração).

Acesse a pasta `src/` e rode o `main.py`.

Ao executar, será mostrado todas as imagens com o desenho criado pelo cascade, para prosseguir cada imagem aperte qualquer tecla. 

O csv com os paths, coordenadas e captions será criado ao final da execução dentro de `src/`

O arquivo `split_train_test.py` serve para separar as imagens que serão utilizadas para treino e teste, com proporção 8:1 respectivamente, podendo ser modificado no mesmo. Esse é o arquivo que retorna o X_train, X_teste, Y_train e Y_teste para prosseguir com o treino do modelo. 