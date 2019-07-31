import cv2

# p1 é uma matriz do tamanho da imagem
# parametro 1 no imread lê a img em preto e branco
p1 = cv2.imread("../static/app.jpg",0)
cv2.imshow("image", p1) 

# dá o valor entre 0 e 255 do pixel
print(p1[0][0]) # 255


cv2.waitKey(0)


