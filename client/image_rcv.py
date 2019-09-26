import numpy
import cv2


def binary_to_image(binary):
    img = binary.reshape((256, 256))
    cv2.imwrite('received.jpg', img)
