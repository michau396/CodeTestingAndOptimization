import cv2
import numpy as np

# 1. Wczytanie obrazu i rozdzielenie kanałów
img = cv2.imread('tower.jpeg')
if img is None:
    print("Nie znaleziono obrazu")
    exit()

b, g, r = cv2.split(img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
cv2.imwrite("blue.jpg", b)
cv2.imwrite("green.jpg", g)
cv2.imwrite("red.jpg", r)

# 2. Porównanie widoczności obiektów w kanałach

# 3. Rekonstrukcja: zamiana R, B, G i wyzerowanie kanału
reversed_rgb = cv2.merge([r, b, g])
no_red = cv2.merge([b, g, np.zeros_like(r)])
cv2.imshow("Zamienione RGB", reversed_rgb)
cv2.imshow("Bez czerwonego", no_red)

# 4. Wzmocnienie kanału czerwonego
r_boosted = cv2.add(r, 50)
img_r_boost = cv2.merge([b, g, r_boosted])
cv2.imshow("Czerwony +50", img_r_boost)

# 5. Maska i wzmocnienie tylko w masce 
mask = np.zeros(img.shape[:2], dtype=np.uint8)
h, w = img.shape[:2]
cv2.rectangle(mask, (w//3, h//3), (2*w//3, 2*h//3), 255, -1)
r_masked = cv2.add(r, 50, mask=mask)
masked_boost = cv2.merge([b, g, r_masked])
cv2.imshow("Czerwony +50 tylko w masce", masked_boost)

# 6. Logo OpenCV – manipulacje
logo = cv2.imread('opencv.png')
if logo is not None:
    lb, lg, lr = cv2.split(logo)
    swapped = cv2.merge([lr, lg, lb])  # niebieski <-> czerwony
    no_green = cv2.merge([lb, np.zeros_like(lg), lr])
    cv2.imshow("Zamieniony kolor logo", swapped)
    cv2.imshow("Logo bez zielonego", no_green)

cv2.waitKey(0)
cv2.destroyAllWindows()
