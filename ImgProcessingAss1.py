import cv2

image = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

negative_gray = 255 - image
 
ret,binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

negative_binary = 255 - binary_image

cv2.imshow("Grayscale", cv2.resize(image, (500, 500)))
cv2.imshow("Negative Grayscale", cv2.resize(negative_gray, (500, 500)))
cv2.imshow("Binary Image", cv2.resize(binary_image, (500, 500)))
cv2.imshow("Negative Binary", cv2.resize(negative_binary, (500, 500)))

cv2.waitKey(0)
cv2.destroyAllWindows()















#Y = 0.299*R + 0.587*G + 0.114*B