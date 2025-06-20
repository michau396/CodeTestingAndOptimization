import cv2
import numpy as np

# 1. Maskowanie twarzy prostokątem
img = cv2.imread('face.jpg')
if img is None:
    print("Nie znaleziono obrazu")
    exit()

mask = np.zeros(img.shape[:2], dtype=np.uint8)
# prostokąt maski 
cv2.rectangle(mask, (100, 100), (300, 300), 255, -1)
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Maska twarz prostokat", result)

# 2. Ukrywanie oczu elipsą
mask2 = np.ones(img.shape[:2], dtype=np.uint8)*255
# elipsa zasłaniająca oczy
cv2.ellipse(mask2, (200, 150), (80, 30), 0, 0, 360, 0, -1)
masked_eyes = cv2.bitwise_and(img, img, mask=mask2)
cv2.imshow("Zaslona oczu", masked_eyes)

# 3. Maskowanie koloru (np. zielony)
img_color = cv2.imread('colour.jpg')
if img_color is None:
    print("Nie znaleziono obrazu kolorowego")
else:
    hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
    # zakres zielonego 
    lower = np.array([40, 40, 40])
    upper = np.array([80, 255, 255])
    mask_color = cv2.inRange(hsv, lower, upper)
    result_color = cv2.bitwise_and(img_color, img_color, mask=mask_color)
    # resztę zaciemniamy czarnym tłem
    black_bg = cv2.bitwise_and(img_color, img_color, mask=cv2.bitwise_not(mask_color))
    black_bg[:] = 0
    final = cv2.add(result_color, black_bg)
    cv2.imshow("Maska koloru zielony", final)

cv2.waitKey(0)
cv2.destroyAllWindows()
