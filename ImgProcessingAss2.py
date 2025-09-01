import cv2
import numpy as np

image = cv2.imread("rgb.png")

#components
B, G, R = cv2.split(image)

zeros = np.zeros_like(G)

blue_component  = cv2.merge([B, zeros, zeros])
green_component = cv2.merge([zeros, G, zeros])
red_component   = cv2.merge([zeros, zeros, R])

cv2.imshow("Original Image", image)
cv2.imshow("Blue Component", blue_component)
cv2.imshow("Green Component", green_component)
cv2.imshow("Red Component", red_component)

cv2.waitKey(0)
cv2.destroyAllWindows()
