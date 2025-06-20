import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Erozja z różnymi strukturami
img1 = cv2.imread('binary.jpg', 0)
if img1 is None:
    print("Nie znaleziono obrazu binarnego")
    exit()

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
erosion_rect = cv2.erode(img1, kernel_rect)
erosion_ellipse = cv2.erode(img1, kernel_ellipse)
cv2.imshow("Erozja RECT", erosion_rect)
cv2.imshow("Erozja ELLIPSE", erosion_ellipse)

# 2. Dylatacja z różnymi iteracjami
img2 = cv2.imread('line.jpg', 0)
kernel = np.ones((3, 3), np.uint8)
results = []
for i in [1, 2, 3, 4, 5]:
    dilated = cv2.dilate(img2, kernel, iterations=i)
    results.append((i, dilated))

# wykres zależności
plt.figure()
for i, (it, im) in enumerate(results):
    plt.subplot(1, 5, i+1)
    plt.title(f"{it}x")
    plt.imshow(im, cmap='gray')
    plt.axis('off')
plt.show()

# 3. Otwarcie - usuwanie szumu
img3 = cv2.imread('noise.jpg', 0)
kernel_open = np.ones((3, 3), np.uint8)
opened = cv2.morphologyEx(img3, cv2.MORPH_OPEN, kernel_open)
cv2.imshow("Przed otwarciem", img3)
cv2.imshow("Po otwarciu", opened)

# 4. Zamknięcie - łączenie liter
img4 = cv2.imread('leters.png', 0)
kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
closed = cv2.morphologyEx(img4, cv2.MORPH_CLOSE, kernel_close)
cv2.imshow("Przed zamknieciem", img4)
cv2.imshow("Po zamknieciu", closed)

# 5. Porównanie struktur dla wielu operacji
img5 = cv2.imread('test.jpg', 0)
shapes = {
    'RECT': cv2.MORPH_RECT,
    'CROSS': cv2.MORPH_CROSS,
    'ELLIPSE': cv2.MORPH_ELLIPSE
}
for name, shape in shapes.items():
    k = cv2.getStructuringElement(shape, (5, 5))
    e = cv2.erode(img5, k)
    d = cv2.dilate(img5, k)
    o = cv2.morphologyEx(img5, cv2.MORPH_OPEN, k)
    c = cv2.morphologyEx(img5, cv2.MORPH_CLOSE, k)
    g = cv2.morphologyEx(img5, cv2.MORPH_GRADIENT, k)
    cv2.imshow(f"{name} Erozja", e)
    cv2.imshow(f"{name} Dylatacja", d)
    cv2.imshow(f"{name} Otwarcie", o)
    cv2.imshow(f"{name} Zamkniecie", c)
    cv2.imshow(f"{name} Gradient", g)

# 6. poprawa obrazu tablicy rejestracyjnej
img6 = cv2.imread('plate.jpg', 0)
blurred = cv2.medianBlur(img6, 3)
clean = cv2.morphologyEx(blurred, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
enhanced = cv2.dilate(clean, np.ones((2, 2), np.uint8))
cv2.imshow("Oryginal", img6)
cv2.imshow("Po morfologii", enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()
