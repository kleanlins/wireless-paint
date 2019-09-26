import cv2
import numpy as np

# p1 é uma matriz do tamanho da imagem
# parametro 1 no imread lê a img em preto e branco


def image_to_binary(filename):
    p1 = cv2.imread(f"../static/{filename}.jpg", 0)
    return p1.flatten()

    # cv2.waitKey(0)
