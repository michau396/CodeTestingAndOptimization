import cv2
import numpy as np

# Tworzenie czarnego obrazu
img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

# Rysowanie trójkąta na img1
pts = np.array([[50, 250], [150, 50], [250, 250]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(img1, [pts], 255)

# Rysowanie okręgu na img2 (można zmienić pozycję)
cv2.circle(img2, (150, 150), 100, 255, -1)

# Operacje bitowe
and_img = cv2.bitwise_and(img1, img2)
or_img = cv2.bitwise_or(img1, img2)
xor_img = cv2.bitwise_xor(img1, img2)
not_img1 = cv2.bitwise_not(img1)

cv2.imshow("Trojkat", img1)
cv2.imshow("Okrag", img2)
cv2.imshow("AND", and_img)
cv2.imshow("OR", or_img)
cv2.imshow("XOR", xor_img)
cv2.imshow("NOT trojkat", not_img1)

# 2. Operacja XOR na dwoch podobnych obrazach
imgA = cv2.imread('cat.jpeg', cv2.IMREAD_GRAYSCALE)
imgB = cv2.imread('dog.jpeg', cv2.IMREAD_GRAYSCALE)
if imgA is None or imgB is None:
    print("Nie znaleziono obrazów do porównania")
else:
    diff = cv2.bitwise_xor(imgA, imgB)
    cv2.imshow("Różnice XOR", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
