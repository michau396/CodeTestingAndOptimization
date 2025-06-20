import cv2
import imutils

img = cv2.imread('snake.webp')
if img is None:
    print("Nie znaleziono obrazu")
    exit()

# 1. Zmniejsz o połowę
small = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
cv2.imshow("Polowa rozmiaru", small)

# 2. Powiększ 2x (INTER_LINEAR)
large = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2), interpolation=cv2.INTER_LINEAR)
cv2.imshow("2x powiekszony", large)

# 3. Zmien rozmiar na 200x300
fixed = cv2.resize(img, (200, 300))
cv2.imshow("200x300", fixed)

# 4. Powieksz 3x różne interpolacje
methods = [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4]
names = ["NEAREST", "LINEAR", "CUBIC", "LANCZOS4"]
for m, n in zip(methods, names):
    resized = cv2.resize(img, (img.shape[1]*3, img.shape[0]*3), interpolation=m)
    cv2.imshow(n, resized)

# 5. Skalowanie do szerokosci 500 z zachowaniem proporcji
resized_width = imutils.resize(img, width=500)
cv2.imshow("Szerokosc 500", resized_width)

# 6. Skalowanie do wysokosci 400 z zachowaniem proporcji
resized_height = imutils.resize(img, height=400)
cv2.imshow("Wysokosc 400", resized_height)

# 7. Zmniejsz 5x INTER_AREA
small_area = cv2.resize(img, (img.shape[1]//5, img.shape[0]//5), interpolation=cv2.INTER_AREA)
cv2.imshow("Zmniejsz 5x INTER_AREA", small_area)

# 8. Powieksz 4x INTER_CUBIC i INTER_LANCZOS4
large_cubic = cv2.resize(img, (img.shape[1]*4, img.shape[0]*4), interpolation=cv2.INTER_CUBIC)
large_lanczos = cv2.resize(img, (img.shape[1]*4, img.shape[0]*4), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Powieksz 4x CUBIC", large_cubic)
cv2.imshow("Powieksz 4x LANCZOS4", large_lanczos)

# 9. Dynamiczne powiekszanie od 100% do 300% co 20%
for scale in range(100, 301, 20):
    factor = scale / 100
    w = int(img.shape[1] * factor)
    h = int(img.shape[0] * factor)
    resized_dyn = cv2.resize(img, (w, h))
    cv2.imshow("Dynamiczne powiekszanie", resized_dyn)
    if cv2.waitKey(500) & 0xFF == 27:
        break

# 10. Powieksz do szerokosci 800 i zapisz
resized_800 = imutils.resize(img, width=800)
cv2.imwrite("resized_output.jpg", resized_800)
cv2.imshow("Szerokosc 800", resized_800)

cv2.waitKey(0)
cv2.destroyAllWindows()
