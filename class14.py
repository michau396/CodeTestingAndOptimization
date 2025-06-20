import cv2
import numpy as np

img = cv2.imread('cat.jpeg')
if img is None:
    print("Nie znaleziono obrazu")
    exit()

# 1. Cztery metody rozmycia z domyślnymi parametrami
blur = cv2.blur(img, (5, 5))
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Blur", blur)
cv2.imshow("GaussianBlur", gaussian)
cv2.imshow("MedianBlur", median)
cv2.imshow("BilateralFilter", bilateral)

# Komentarze:
# - MedianBlur najlepiej usuwa szum
# - BilateralFilter najlepiej zachowuje krawędzie
# - Blur i Gaussian rozmywają wszystko, ale są szybkie

# 2. Efekt zmiany kernela
kernels = [3, 5, 9, 15]
for k in kernels:
    cv2.imshow(f"Blur {k}x{k}", cv2.blur(img, (k, k)))
    cv2.imshow(f"Gaussian {k}x{k}", cv2.GaussianBlur(img, (k, k), 0))
    if k % 2 == 1:
        cv2.imshow(f"Median {k}", cv2.medianBlur(img, k))

# Komentarze:
# - Im większy kernel, tym silniejsze rozmycie, ale więcej detali ginie
# - Dla redukcji szumu bez utraty jakości najlepsze są median 5 i bilateral

# 3. BilateralFilter – różne parametry
bil1 = cv2.bilateralFilter(img, 5, 25, 25)
bil2 = cv2.bilateralFilter(img, 9, 75, 75)
bil3 = cv2.bilateralFilter(img, 15, 150, 150)

cv2.imshow("Bilateral 5", bil1)
cv2.imshow("Bilateral 9", bil2)
cv2.imshow("Bilateral 15", bil3)

# Komentarze:
# - Rozmycie dwustronne dobrze redukuje szum i zachowuje krawędzie
# - Bilateral działa wolniej, ale daje najlepszy balans jakość/szum/krawędź

# 4. Tekst na obrazie
tekst = cv2.imread('text.jpg')
if tekst is not None:
    cv2.imshow("Text - blur", cv2.blur(tekst, (5, 5)))
    cv2.imshow("Text - gaussian", cv2.GaussianBlur(tekst, (5, 5), 0))
    cv2.imshow("Text - median", cv2.medianBlur(tekst, 5))
    cv2.imshow("Text - bilateral", cv2.bilateralFilter(tekst, 9, 75, 75))

# Komentarze:
# - Blur/gaussian mocno niszczą czytelność tekstu
# - Median i bilateral pozwalają zachować więcej konturów liter

# 5. Dodanie szumu i porównanie metod
img_noise = img.copy()
cv2.randn(img_noise, 128, 20)  # szum gaussowski
noisy = cv2.add(img, img_noise)

cv2.imshow("Noisy", noisy)
cv2.imshow("Noisy - blur", cv2.blur(noisy, (5, 5)))
cv2.imshow("Noisy - gaussian", cv2.GaussianBlur(noisy, (5, 5), 0))
cv2.imshow("Noisy - median", cv2.medianBlur(noisy, 5))
cv2.imshow("Noisy - bilateral", cv2.bilateralFilter(noisy, 9, 75, 75))

# Komentarze:
# - Median najlepiej działa na szum solno-pieprzowy
# - Gaussian sprawdza się przy szumie gaussowskim
# - Bilateral jest najbardziej uniwersalny i zachowuje szczegóły

# 6. Efekt głębi ostrości (rozmycie tła)
img_focus = img.copy()
mask = np.zeros(img.shape[:2], dtype="uint8")
h, w = mask.shape
cv2.circle(mask, (w // 2, h // 2), 100, 255, -1)
blurred_bg = cv2.GaussianBlur(img_focus, (21, 21), 0)
foreground = cv2.bitwise_and(img_focus, img_focus, mask=mask)
background = cv2.bitwise_and(blurred_bg, blurred_bg, mask=cv2.bitwise_not(mask))
depth_effect = cv2.add(foreground, background)
cv2.imshow("Depth of field", depth_effect)

# Komentarz:
# - Rozmycie tła symuluje efekt fotograficzny — główny obiekt pozostaje ostry

cv2.waitKey(0)
cv2.destroyAllWindows()
