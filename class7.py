import cv2
import numpy as np

img = cv2.imread('tower.jpeg')
if img is None:
    print("Nie znaleziono obrazu")
    exit()

flip_h = cv2.flip(img, 1)   # odbicie poziome
flip_v = cv2.flip(img, 0)   # odbicie pionowe
flip_both = cv2.flip(img, -1)  # odbicie względem obu osi

cv2.imshow("Oryginal", img)
cv2.imshow("Odbicie poziome", flip_h)
cv2.imshow("Odbicie pionowe", flip_v)
cv2.imshow("Odbicie obu osi", flip_both)

# Wycięcie fragmentu (środek) i odbicie tylko jego
h, w = img.shape[:2]
x1, y1 = w//4, h//4
x2, y2 = w*3//4, h*3//4
fragment = img[y1:y2, x1:x2]
fragment_flipped = cv2.flip(fragment, 1)
img[y1:y2, x1:x2] = fragment_flipped
cv2.imshow("Obraz z odbitym fragmentem", img)

# Wybór odbicia od użytkownika
choice = int(input("Wybierz odbicie (0-pionowe,1-poziome,-1-obustronne): "))
result = cv2.flip(img, choice)
cv2.imshow("Wybrane odbicie", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
